from abc import ABC, abstractmethod


class ApiContext(ABC):

    @abstractmethod
    def get_identity(self):
        pass
