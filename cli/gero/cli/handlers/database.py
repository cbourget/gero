from gero.app.contexts.cli import CliContext
from gero.app.database.manager import DatabaseManager
from gero.cli.cli import CLI_HANDLER


class DatabaseHandler:

    def __init__(self, manager: DatabaseManager):
        self._manager = manager

    def init(self):
        self._manager.initialize()
        return 'Database initialized successfully'

    def reset(self):
        self._manager.reset()
        return 'Database reset successfully'


def bootstrap(app):
    app.register_factory(
        DatabaseHandler,
        (CLI_HANDLER, 'database'),
        ctx_iface=CliContext)
