from gero.app.iam.user.service import UserService
from gero.app.iam.identity.service import IdentityService

from gero.api.auth.strategy import AuthStrategy


class AuthService:

    def __init__(
        self,
        auth_strategy: AuthStrategy,
        user_service: UserService,
        identity_service: IdentityService):

        self._auth_strategy = auth_strategy
        self._user_service = user_service
        self._identity_service = identity_service

    def signin(self, request, response, body, login, password):
        user = self._user_service.one_by_id(1)
        self._auth_strategy.encode_claims(request, response, body, {
            'user_id': user.id
        })
        return self._identity_service.get_user_identity(user)

    def get_identity_from_request(self, request):
        claims = self._auth_strategy.decode_claims(request)
        user_id = claims.get('user_id')
        if user_id is None:
            user = None
        else:
            user = self._user_service.one_by_id(user_id)
        return self._identity_service.get_user_identity(user)


def bootstrap(app, api):
    app.register_factory(AuthService)
