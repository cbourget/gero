from capri.alchemy.database import Database

from gero.app.database.data.store import DatabaseDataSourceStore
from gero.app.database.entity.middleware import DatabaseEntityMiddleware


def database_data_source_store_entity_middleware_factory(context):
    database = context.get_instance(Database)
    principals_table_name = context.settings.get(
        'database.tables.data_source_principal')
    principals_table = database.metadata.tables[principals_table_name]
    return DatabaseEntityMiddleware(database, principals_table, 'datasource_id')


def bootstrap(app):
    app.register_factory(
        database_data_source_store_entity_middleware_factory,
        (DatabaseDataSourceStore, 'middleware', 'entity'))
