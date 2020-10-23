from abc import ABC, abstractmethod


class IPolicyStore(ABC):

    @abstractmethod
    def one_by_id(self, policy_id):
        pass

    @abstractmethod
    def get_roles_policies(self, roles, scope=None, permission=None):
        pass

    @abstractmethod
    def create(self, policy):
        pass

    @abstractmethod
    def update(self, policy):
        pass

    @abstractmethod
    def delete(self, policy):
        pass
