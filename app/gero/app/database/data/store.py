from sqlalchemy.sql import select

from gero.app.database import Database
from capri.core.injector import InjectionError

from gero.app.domain.data.model import DataSource
from gero.app.domain.data.store import IDataSourceStore
from gero.app.utils import middleware


class DataSourceStore(IDataSourceStore):

    def __init__(
        self,
        database,
        middlewares=None,
        identity=None):

        self._database = database
        self._data_source_table = database['data_source']
        self._middlewares = middlewares if middlewares is not None else []
        self._identity = identity

     # Mappers

    def _row_to_data_source(self, row):
        return DataSource(row.id, row.type)

    def _data_source_to_row(self, data_source):
        return {
            'id': data_source.id,
            'type': data_source.type
        }

    ## Read ##

    def one_by_id(self, data_source_id):
        query = select([
            self._data_source_table
        ]).where(self._data_source_table.c.id == data_source_id)
        query = self._prepare_query(query, self._identity)

        row = self._database.execute(query).first()

        if row:
            return self._row_to_data_source(row)
        return None

    @middleware.hook
    def _prepare_query(self, query, identity):
        return query

    ## CUD ##

    def create(self, data_source):
        row = self._data_source_to_row(data_source)
        insert = self._data_source_table.insert().values(**row)
        self._database.execute(insert)

        return data_source

    def update(self, data_source):
        row = self._data_source_to_row(data_source)
        update = self._data_source_table.update().where(
            self._data_source_table.c.id == data_source.id
        ).values(**row)
        self._database.execute(update)

        return data_source

    def delete(self, data_source):
        delete = self._data_source_table.delete().where(
            self._data_source_table.c.id == data_source.id
        )
        self._database.execute(delete)


def data_source_store_factory(context):
    database = context.get_instance(Database)

    try:
        middlewares = [m for m, t in context.get_instances(
            (DataSourceStore, 'middleware'))]
    except InjectionError:
        middlewares = []

    return DataSourceStore(
        database,
        middlewares=middlewares,
        identity=context.get_identity())


def bootstrap(app):
    app.register_factory(data_source_store_factory, IDataSourceStore)
