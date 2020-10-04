from abc import ABC, abstractmethod


class DataSourceStore(ABC):

    @abstractmethod
    def one_by_id(self, data_source_id):
        pass

    @abstractmethod
    def create(self, data_source):
        pass

    @abstractmethod
    def update(self, data_source):
        pass

    @abstractmethod
    def delete(self, data_source):
        pass
