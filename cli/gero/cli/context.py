from capri.core.context import AppContext

from gero.app.contexts.cli import CliContext as ICliContext


class CliContext(AppContext, ICliContext):

    def __init__(self, settings, providers):
        super().__init__(settings, providers)
        self._identity = None

    def get_identity(self):
        return self._identity


def create_cli_context(app):
    return app.create_context(CliContext, ICliContext)
