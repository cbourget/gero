from capri.core.context import AppContext

from gero.app.contexts.api import ApiContext as IApiContext
from gero.api.auth.service import AuthService


class ApiContext(AppContext, IApiContext):

    def __init__(self, settings, providers, request):
        super().__init__(settings, providers)
        self._request = request
        self._identity = None

    def get_identity(self):
        if self._identity is None:
            auth_service = self.get_instance(AuthService)
            self._identity = \
                auth_service.get_identity_from_request(self._request)
        return self._identity
