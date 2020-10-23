from gero.app.contexts.cli import CliContext
from gero.app.domain.data import (
    get_data_source,
    create_data_source,
    update_data_source,
    delete_data_source)
from gero.app.domain.data.service import DataSourceService
from gero.cli.cli import CLI_HANDLER


class DataSourceHandler:

    def __init__(self, context):
        self._context = context

    def get(self, id):
        data_source = get_data_source(self._context, id)
        if not data_source:
            return None
        return data_source.dump()

    def create(self, data):
        data_source = create_data_source(self._context, data)
        return data_source.dump()

    def update(self, data):
        data_source = update_data_source(self._context, data)
        return data_source.dump()

    def delete(self, id):
        delete_data_source(self._context, id)


class DataSourceUnavailableHandler:
    """
    These methods are currently unavailable.
    This is most likely because no data_sources table was found in the database.
    """


def data_source_handler_factory(context):
    try:
        context.get_instance(DataSourceService)
    except KeyError:
        return DataSourceUnavailableHandler()
    return DataSourceHandler(context)


def bootstrap(app):
    app.register_factory(
        data_source_handler_factory,
        (CLI_HANDLER, 'data'),
        ctx_iface=CliContext)
