from gero.app.contexts.cli import CliContext
from gero.app.database.manager import DatabaseManager
from gero.cli.cli import CLI_HANDLER


class DatabaseHandler:

    def __init__(self, manager):
        self._manager = manager

    def initialize(self):
        self._manager.initialize()
        return 'Database initialized successfully'

    def reset(self):
        self._manager.reset()
        return 'Database reset successfully'


def database_handler_factory(context):
    manager = context.get_instance(DatabaseManager)
    return DatabaseHandler(manager)


def bootstrap(app):
    app.register_factory(
        database_handler_factory,
        (CLI_HANDLER, 'database'),
        ctx_iface=CliContext)
