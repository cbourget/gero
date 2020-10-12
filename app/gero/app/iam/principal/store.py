from abc import ABC, abstractmethod


class IPrincipalStore(ABC):

    @abstractmethod
    def one_by_id(self, principal_id):
        pass

    @abstractmethod
    def create(self, principal):
        pass

    @abstractmethod
    def update(self, principal):
        pass

    @abstractmethod
    def delete(self, principal):
        pass
