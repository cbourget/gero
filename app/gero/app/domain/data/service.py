from gero.app.domain.data.model import DataSource
from gero.app.domain.data.store import DataSourceStore


class DataSourceService:

    def __init__(self, data_source_store):
        self._data_source_store = data_source_store

    ## Read ##

    def one_by_id(self, data_source_id):
        return self._data_source_store.one_by_id(data_source_id)

    ## CUD ##

    def create(self, data):
        data_source = DataSource(
            data['id'],
            data['type']
        )
        return self._data_source_store.create(data_source)

    def update(self, data):
        data_source = DataSource(
            data['id'],
            data['type']
        )
        return self._data_source_store.update(data_source)

    def delete(self, data_source_id):
        data_source = DataSource(
            data_source_id,
            None
        )
        self._data_source_store.delete(data_source)


def data_source_service_factory(context):
    data_source_store = context.get_instance(DataSourceStore)
    return DataSourceService(data_source_store)


def bootstrap(app):
    app.register_factory(data_source_service_factory, DataSourceService)
