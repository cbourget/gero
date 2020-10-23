from abc import ABC, abstractmethod


class IGroupStore(ABC):

    @abstractmethod
    def one_by_id(self, group_id):
        pass

    @abstractmethod
    def get_user_groups(self, user):
        pass

    @abstractmethod
    def create(self, group):
        pass

    @abstractmethod
    def update(self, group):
        pass

    @abstractmethod
    def delete(self, group):
        pass
