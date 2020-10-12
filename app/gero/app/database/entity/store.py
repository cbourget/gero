from sqlalchemy.sql import select

from capri.alchemy.database import Database

from gero.app.iam.entity.model import Entity
from gero.app.iam.entity.store import IEntityStore


class EntityStore(IEntityStore):

    def __init__(self, database, entity_table):
        self._database = database
        self._entity_table = entity_table

     # Mappers

    def _row_to_entity(self, row):
        return Entity(row.id, row.type)

    def _entity_to_row(self, entity):
        return {
            'id': entity.id,
            'type': entity.type
        }

    ## Read ##

    def one_by_id(self, entity_id):
        query = select([
            self._entity_table
        ]).where(self._entity_table.c.id == entity_id)
        row = self._database.execute(query).first()

        if row:
            return self._row_to_entity(row)
        return None

    ## CUD ##

    def create(self, entity):
        row = self._entity_to_row(entity)
        insert = self._entity_table.insert().values(**row)
        self._database.execute(insert)

        return entity

    def update(self, entity):
        row = self._entity_to_row(entity)
        update = self._entity_table.update().where(
            self._entity_table.c.id == entity.id
        ).values(**row)
        self._database.execute(update)

        return entity

    def delete(self, entity):
        delete = self._entity_table.delete().where(
            self._entity_table.c.id == entity.id
        )
        self._database.execute(delete)


def entity_store_factory(context):
    database = context.get_instance(Database)
    entity_table_name = context.settings.get(
        'database.tables.entity')
    entity_table = database.metadata.tables[entity_table_name]
    return EntityStore(database, entity_table)


def bootstrap(app):
    app.register_factory(entity_store_factory, IEntityStore)
