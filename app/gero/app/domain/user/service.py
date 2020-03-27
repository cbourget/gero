from gero.app.domain.user.model import User
from gero.app.domain.user.store import UserStore


class UserService:

    def __init__(self, user_store):
        self._user_store = user_store

    def one_by_id(self, user_id):
        return self._user_store.one_by_id(user_id)

    def create(self, data):
        user = User(
            data['id']
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
        return self._user_store.delete(user)


def user_service_factory(context):
    user_store = context.get_instance(UserStore)
    return UserService(user_store)


def bootstrap(app):
    app.register_factory(user_service_factory, UserService)
