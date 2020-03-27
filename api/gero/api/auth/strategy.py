from abc import ABC, abstractmethod


class AuthStrategy(ABC):
    
    @abstractmethod
    def decode_claims(self, request):
        pass

    @abstractmethod
    def encode_claims(self, request, response, body, claims):
        pass
