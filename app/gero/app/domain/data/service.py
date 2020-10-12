from gero.app.iam.entity.service import EntityService
from gero.app.iam.data.model import DataSource
from gero.app.iam.data.store import IDataSourceStore


class DataSourceService:

    def __init__(self, data_source_store, entity_service):
        self._data_source_store = data_source_store
        self._entity_service = entity_service

    ## Read ##

    def one_by_id(self, data_source_id):
        return self._data_source_store.one_by_id(data_source_id)

    ## CUD ##

    def create(self, data):
        entity = self._entity_service.create({
            'id': data['id'],
            'type': 'data_source'
        })
        data_source = DataSource(
            entity.id,
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
            data_source_id
        )
        self._data_source_store.delete(data_source)
        self._entity_service.delete(data_source_id)


def data_source_service_factory(context):
    data_source_store = context.get_instance(IDataSourceStore)
    entity_service = context.get_instance(EntityService)
    return DataSourceService(data_source_store, entity_service)


def bootstrap(app):
    app.register_factory(data_source_service_factory, DataSourceService)
