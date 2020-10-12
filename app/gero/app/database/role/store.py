from sqlalchemy.sql import select

from capri.alchemy.database import Database

from gero.app.iam.role.model import Role
from gero.app.iam.role.store import IRoleStore


class RoleStore(IRoleStore):

    def __init__(self, database, role_table, principal_role_table):
        self._database = database
        self._role_table = role_table
        self._principal_role_table = principal_role_table

    # Mappers

    def _row_to_role(self, row):
        return Role(row.id, row.name)

    def _role_to_row(self, role):
        return {
            'id': role.id,
            'name': role.name
        }

    ## Read ##

    def one_by_id(self, role_id):
        query = select([
            self._role_table
        ]).where(self._role_table.c.id == role_id)
        row = self._database.execute(query).first()

        if row:
            return self._row_to_role(row)
        return None

    def get_principals_roles(self, principals):
        if not principals:
            return []

        query = self._query_roles_by_principals(principals)

        return [
            self._row_to_role(row)
            for row in self._database.execute(query)
        ]

    def _query_roles_by_principals(self, principals):
        return select([
            self._role_table
        ]).select_from(
            self._role_table.join(
                self._principal_role_table,
                self._role_table.c.id == self._principal_role_table.c.role_id
            )
        ).where(
            self._principal_role_table.c.principal_id.in_(
                [p.id for p in principals]
            )
        )

    ## CUD ##

    def create(self, role):
        row = self._role_to_row(role)
        insert = self._role_table.insert().values(**row)
        self._database.execute(insert)

        return role

    def update(self, role):
        row = self._role_to_row(role)
        update = self._role_table.update().where(
            self._role_table.c.id == role.id
        ).values(**row)
        self._database.execute(update)

        return role

    def delete(self, role):
        delete = self._role_table.delete().where(
            self._role_table.c.id == role.id
        )
        self._database.execute(delete)


def role_store_factory(context):
    database = context.get_instance(Database)
    role_table_name = context.settings.get(
        'database.table.role')
    role_table = database.metadata.tables[role_table_name]
    principal_role_table_name = context.settings.get(
        'database.table.principal_role')
    principal_role_table = database.metadata.tables[principal_role_table_name]
    return RoleStore(database, role_table, principal_role_table)


def bootstrap(app):
    app.register_factory(role_store_factory, IRoleStore)
