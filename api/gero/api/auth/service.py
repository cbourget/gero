from gero.app.domain.user.service import UserService
from gero.app.identity import Identity

from gero.api.auth.strategy import AuthStrategy


class AuthService:

    def __init__(self, auth_strategy, user_service):
        self._auth_strategy = auth_strategy
        self._user_service = user_service

    def signin(self, request, response, body, login, password):
        user = self._user_service.one_by_id(1)
        identity = Identity(user)
        self._auth_strategy.encode_claims(request, response, body, {
            'user_id': user.id
        })
        return identity

    def get_identity(self, request):
        claims = self._auth_strategy.decode_claims(request)
        user_id = claims.get('user_id')
        if user_id is None:
            user = None
        else:
            user = self._user_service.one_by_id(user_id)
        return Identity(user)


def auth_service_factory(context):
    auth_strategy = context.get_instance(AuthStrategy)
    user_service = context.get_instance(UserService)
    return AuthService(auth_strategy, user_service)


def bootstrap(app, api):
    app.register_factory(auth_service_factory, AuthService)
