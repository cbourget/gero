from abc import ABC, abstractmethod


class IUserStore(ABC):

    @abstractmethod
    def one_by_id(self, user_id):
        pass

    @abstractmethod
    def create(self, user):
        pass

    @abstractmethod
    def update(self, user):
        pass

    @abstractmethod
    def delete(self, user):
        pass
