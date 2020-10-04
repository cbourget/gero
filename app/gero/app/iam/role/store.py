from abc import ABC, abstractmethod


class RoleStore(ABC):

    @abstractmethod
    def one_by_id(self, role_id):
        pass

    @abstractmethod
    def get_principals_roles(self, principals):
        pass

    @abstractmethod
    def create(self, role):
        pass

    @abstractmethod
    def update(self, role):
        pass

    @abstractmethod
    def delete(self, role):
        pass
