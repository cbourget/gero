from sqlalchemy import or_
from sqlalchemy.sql import select

from capri.alchemy.database import Database

from gero.app.iam.policy.model import Policy
from gero.app.iam.policy.store import IPolicyStore


class PolicyStore(IPolicyStore):

    def __init__(self, database, policy_table, role_policy_table):
        self._database = database
        self._policy_table = policy_table
        self._role_policy_table = role_policy_table

    # Mappers

    def _row_to_policy(self, row):
        return Policy(
            row.id,
            row.name,
            row.scope,
            row.action,
            row.subset,
            row.attribution)

    def _policy_to_row(self, policy):
        return {
            'id': policy.id,
            'name': policy.name,
            'scope': policy.scope,
            'action': policy.action,
            'subset': policy.subset,
            'attribution': policy.attribution
        }

    ## Read ##

    def one_by_id(self, policy_id):
        query = select([
            self._policy_table
        ]).where(self._policy_table.c.id == policy_id)
        row = self._database.execute(query).first()

        if row:
            return self._row_to_policy(row)
        return None

    def get_roles_policies(self, roles, scope=None, permission=None):
        if not roles:
            return []

        query = self._query_policies_by_roles(
            roles, scope, permission
        )

        return [
            self._row_to_policy(row)
            for row in self._database.execute(query)
        ]

    def _query_policies_by_roles(self, roles, scope, permission):
        query = select([
            self._policy_table.c.id,
            self._policy_table.c.name,
            self._policy_table.c.entity,
            self._policy_table.c.action,
            self._policy_table.c.subset,
            self._policy_table.c.attribution
        ]).select_from(
            self._policy_table.join(
                self._role_policy_table,
                self._policy_table.c.id == self._role_policy_table.c.policy_id
            )
        ).where(
            self._role_policy_table.c.role_id.in_([r.id for r in roles])
        )

        if scope is not None:
            query = query.where(
                or_(
                    self._policy_table.c.entity == scope,
                    self._policy_table.c.entity == '*'
                )
            )

        if permission is not None:
            query = query.where(
                self._policy_table.c.permission == permission
            )

        return query

    ## CUD ##

    def create(self, policy):
        row = self._policy_to_row(policy)
        insert = self._policy_table.insert().values(**row)
        self._database.execute(insert)

        return policy

    def update(self, policy):
        row = self._policy_to_row(policy)
        update = self._policy_table.update().where(
            self._policy_table.c.id == policy.id
        ).values(**row)
        self._database.execute(update)

        return policy

    def delete(self, policy):
        delete = self._policy_table.delete().where(
            self._policy_table.c.id == policy.id
        )
        self._database.execute(delete)


def policy_store_factory(context):
    database = context.get_instance(Database)
    policy_table_name = context.settings.get(
        'database.tables.policy')
    policy_table = database.metadata.tables[policy_table_name]
    role_policy_table_name = context.settings.get(
        'database.tables.role_policy')
    role_policy_table = database.metadata.tables[role_policy_table_name]
    return PolicyStore(database, policy_table, role_policy_table)


def bootstrap(app):
    app.register_factory(policy_store_factory, IPolicyStore)
