from sqlalchemy import MetaData, create_engine
from sqlalchemy.engine import Engine

from capri.alchemy.database import Database as CapriDatabase


class Database(CapriDatabase):

    def __init__(self, engine, metadata, mapper):
        super().__init__(engine, metadata)
        self.mapper = mapper

    def __getitem__(self, key):
        return self.get_table(key)

    def get_table(self, key):
        table_name = self.mapper[key]
        return self.metadata.tables[table_name] 


def database_factory(context):
    engine = context.get_instance(Engine)
    metadata = context.get_instance(MetaData)
    mapper = context.settings.get('database.tables', {})
    return Database(engine, metadata, mapper)


def bootstrap(app):
    connection_str = app.settings.get('database.connection')
    engine = create_engine(connection_str)
    metadata = MetaData(engine)
    metadata.reflect()

    app.register_instance(engine, Engine)
    app.register_instance(metadata, MetaData)
    app.register_factory(database_factory, Database)

    app.include('.manager')

    # IAM
    app.include('.entity')
    app.include('.group')
    app.include('.policy')
    app.include('.principal')
    app.include('.role')
    app.include('.user')

    # Domain
    app.include('.data')
