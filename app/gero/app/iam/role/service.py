from gero.app.iam.role.store import IRoleStore


class RoleService:

    def __init__(self, role_store: IRoleStore):
        self._role_store = role_store

    ## Read ##

    def one_by_id(self, role_id):
        return self._role_store.one_by_id(role_id)

    def get_principals_roles(self, principals):
        return self._role_store.get_principals_roles(principals)


def bootstrap(app):
    app.register_factory(RoleService)
