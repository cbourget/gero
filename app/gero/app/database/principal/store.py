from sqlalchemy.sql import select

from capri.alchemy.database import Database

from gero.app.iam.principal.model import Principal
from gero.app.iam.principal.store import IPrincipalStore


class PrincipalStore(IPrincipalStore):

    def __init__(self, database, principal_table):
        self._database = database
        self._principal_table = principal_table

     # Mappers

    def _row_to_principal(self, row):
        return Principal(row.id, row.type)

    def _principal_to_row(self, principal):
        return {
            'id': principal.id,
            'type': principal.type
        }

    ## Read ##

    def one_by_id(self, principal_id):
        query = select([
            self._principal_table
        ]).where(self._principal_table.c.id == principal_id)
        row = self._database.execute(query).first()

        if row:
            return self._row_to_principal(row)
        return None

    ## CUD ##

    def create(self, principal):
        row = self._principal_to_row(principal)
        insert = self._principal_table.insert().values(**row)
        self._database.execute(insert)

        return principal

    def update(self, principal):
        row = self._principal_to_row(principal)
        update = self._principal_table.update().where(
            self._principal_table.c.id == principal.id
        ).values(**row)
        self._database.execute(update)

        return principal

    def delete(self, principal):
        delete = self._principal_table.delete().where(
            self._principal_table.c.id == principal.id
        )
        self._database.execute(delete)


def principal_store_factory(context):
    database = context.get_instance(Database)
    principal_table_name = context.settings.get(
        'database.tables.principal')
    principal_table = database.metadata.tables[principal_table_name]
    return PrincipalStore(database, principal_table)


def bootstrap(app):
    app.register_factory(principal_store_factory, IPrincipalStore)
