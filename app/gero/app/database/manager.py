from sqlalchemy import (
    Boolean,
    Column,
    ForeignKey,
    Integer,
    Text,
    Table
)

from capri.alchemy.database import Database

from gero.app.contexts.cli import CliContext


class DatabaseManager:

    def __init__(self, database, tables):
        self._database = database
        self._tables = tables

    def initialize(self):
        self._create_user_table()

    def _create_user_table(self):
        tbl_users = Table(
            self._tables.get('user', 'users'),
            self._database.metadata,
            Column('id', Integer, primary_key=True))
        tbl_users.create(self._database.engine)


def database_manager_factory(context):
    database = context.get_instance(Database)
    tables = context.settings.get('database.tables', {})
    return DatabaseManager(database, tables)


def bootstrap(app):
    app.register_factory(
        database_manager_factory,
        DatabaseManager,
        ctx_iface=CliContext)
