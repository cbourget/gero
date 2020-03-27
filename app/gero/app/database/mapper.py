from abc import ABC, abstractmethod


class DatabaseMapper(ABC):

    @abstractmethod
    def row_to_instance(self, row):
        pass

    @abstractmethod
    def instance_to_insert(self, instance):
        pass

    @abstractmethod
    def instance_to_update(self, instance):
        pass
