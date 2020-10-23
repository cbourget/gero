from gero.app.database import Database

from gero.app.database.data.store import DataSourceStore
from gero.app.database.entity.middleware import EntityMiddleware


def data_source_store_entity_middleware_factory(database: Database):
    return EntityMiddleware(
        database,
        database['data_source_principal'],
        'datasource_id')


def bootstrap(app):
    app.register_factory(
        data_source_store_entity_middleware_factory,
        (DataSourceStore, 'middleware', 'entity'))
