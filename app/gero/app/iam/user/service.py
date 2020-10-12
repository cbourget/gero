from gero.app.iam.principal.service import PrincipalService
from gero.app.iam.user.model import User
from gero.app.iam.user.store import IUserStore


class UserService:

    def __init__(self, user_store, principal_service):
        self._user_store = user_store
        self._principal_service = principal_service

    ## Read ##

    def one_by_id(self, user_id):
        return self._user_store.one_by_id(user_id)

    ## CUD ##

    def create(self, data):
        principal = self._principal_service.create({
            'id': data['id'],
            'type': 'user'
        })
        user = User(
            principal.id
        )
        return self._user_store.create(user)

    def update(self, data):
        user = User(
            data['id']
        )
        return self._user_store.update(user)

    def delete(self, user_id):
        user = User(
            user_id
        )
        self._user_store.delete(user)
        self._principal_service.delete(user_id)


def user_service_factory(context):
    user_store = context.get_instance(IUserStore)
    principal_service = context.get_instance(PrincipalService)
    return UserService(user_store, principal_service)


def bootstrap(app):
    app.register_factory(user_service_factory, UserService)
