from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine

from capri.alchemy.database import Database


def database_factory(context):
    engine = context.get_instance(Engine)
    metadata = context.get_instance(MetaData)
    return Database(engine, metadata)


def bootstrap(app):
    connection_str = app.settings.get('database.connection')
    engine = create_engine(connection_str)
    metadata = MetaData(engine)
    metadata.reflect()

    app.register_instance(engine, Engine)
    app.register_instance(metadata, MetaData)
    app.register_factory(database_factory, Database)

    app.include('.user')
    app.include('.manager')
