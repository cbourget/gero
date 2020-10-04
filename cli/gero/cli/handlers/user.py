from gero.app.contexts.cli import CliContext
from gero.app.iam.user import get_user, create_user, update_user, delete_user
from gero.app.iam.user.service import UserService
from gero.cli.cli import CLI_HANDLER

"""
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
"""

class UserHandler:

    def __init__(self, context):
        self._context = context

    def get(self, id):
        user = get_user(self._context, id)
        if not user:
            return None
        return user.dump()

    def create(self, data):
        user = create_user(self._context, data)
        return user.dump()

    def update(self, data):
        user = update_user(self._context, data)
        return user.dump()

    def delete(self, id):
        delete_user(self._context, id)


class UserUnavailableHandler:
    """
    These methods are currently unavailable.
    This is most likely because no users table was found in the database.
    """

"""
def user_handler_factory(context):
    try:
        service = context.get_instance(UserService)
    except KeyError:
        return UserUnavailableHandler()
    return UserHandler(service)
"""

def user_handler_factory(context):
    try:
        context.get_instance(UserService)
    except KeyError:
        return UserUnavailableHandler()
    return UserHandler(context)


def bootstrap(app):
    app.register_factory(
        user_handler_factory,
        (CLI_HANDLER, 'user'),
        ctx_iface=CliContext)
