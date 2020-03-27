from gero.app.contexts.cli import CliContext
from gero.app.domain.user.service import UserService
from gero.cli.cli import CLI_HANDLER


class UserHandler:

    def __init__(self, service):
        self._service = service

    def get(self, id):
        user = self._service.one_by_id(id)
        return user.dump() if user else None

    def create(self, data):
        user = self._service.create(data)
        return user.dump()

    def update(self, data):
        user = self._service.update(data)
        return user.dump()

    def delete(self, id):
        self._service.delete(id)


class UserUnavailableHandler:
    """
    These methods are currently unavailable.
    This is most likely because no users table was found in the database.
    """


def user_handler_factory(context):
    try:
        service = context.get_instance(UserService)
    except KeyError:
        return UserUnavailableHandler()
    return UserHandler(service)


def bootstrap(app):
    app.register_factory(
        user_handler_factory,
        (CLI_HANDLER, 'user'),
        ctx_iface=CliContext)
