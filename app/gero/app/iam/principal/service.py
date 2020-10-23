from gero.app.iam.principal.model import Principal
from gero.app.iam.principal.store import IPrincipalStore


class PrincipalService:

    def __init__(self, principal_store: IPrincipalStore):
        self._principal_store = principal_store

    ## Read ##

    def one_by_id(self, principal_id):
        return self._principal_store.one_by_id(principal_id)

    ## CUD ##

    def create(self, data):
        principal = Principal(
            data['id'],
            data['type']
        )
        return self._principal_store.create(principal)

    def update(self, data):
        principal = Principal(
            data['id'],
            data['type']
        )
        return self._principal_store.update(principal)

    def delete(self, principal_id):
        principal = Principal(
            principal_id,
            None
        )
        self._principal_store.delete(principal)


def bootstrap(app):
    app.register_factory(PrincipalService)
