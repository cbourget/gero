from gero.app.iam.entity.model import Entity
from gero.app.iam.entity.store import IEntityStore


class EntityService:

    def __init__(self, entity_store):
        self._entity_store = entity_store

    ## Read ##

    def one_by_id(self, entity_id):
        return self._entity_store.one_by_id(entity_id)

    ## CUD ##

    def create(self, data):
        entity = Entity(
            data['id'],
            data['type']
        )
        return self._entity_store.create(entity)

    def update(self, data):
        entity = Entity(
            data['id'],
            data['type']
        )
        return self._entity_store.update(entity)

    def delete(self, entity_id):
        entity = Entity(
            entity_id,
            None
        )
        self._entity_store.delete(entity)


def entity_service_factory(context):
    entity_store = context.get_instance(IEntityStore)
    return EntityService(entity_store)


def bootstrap(app):
    app.register_factory(entity_service_factory, EntityService)
