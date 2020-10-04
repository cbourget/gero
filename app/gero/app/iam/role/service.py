from gero.app.iam.role.store import RoleStore


class RoleService:

    def __init__(self, role_store):
        self._role_store = role_store

    ## Read ##

    def one_by_id(self, role_id):
        return self._role_store.one_by_id(role_id)

    def get_principals_roles(self, principals):
        return self._role_store.get_principals_roles(principals)


def role_service_factory(context):
    role_store = context.get_instance(RoleStore)
    return RoleService(role_store)


def bootstrap(app):
    app.register_factory(role_service_factory, RoleService)
