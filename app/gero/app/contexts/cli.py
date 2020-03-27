from abc import ABC, abstractmethod
from capri.core.context import AppContext


class CliContext(ABC):
    
    @abstractmethod
    def get_identity(self):
        pass
