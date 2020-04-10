from abc import ABC, abstractmethod


class CliContext(ABC):

    @abstractmethod
    def get_identity(self):
        pass
