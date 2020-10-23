from abc import ABC, abstractmethod


class IEntityStore(ABC):

    @abstractmethod
    def one_by_id(self, entity_id):
        pass

    @abstractmethod
    def create(self, entity):
        pass

    @abstractmethod
    def update(self, entity):
        pass

    @abstractmethod
    def delete(self, entity):
        pass
