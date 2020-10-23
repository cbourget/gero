from gero.app.iam.principal.service import PrincipalService
from gero.app.iam.group.model import Group
from gero.app.iam.group.store import IGroupStore


class GroupService:

    def __init__(
        self,
        group_store: IGroupStore,
        principal_service: PrincipalService):

        self._group_store = group_store
        self._principal_service = principal_service

    ## Read ##

    def one_by_id(self, group_id):
        return self._group_store.one_by_id(group_id)

    def get_user_groups(self, user):
        return self._group_store.get_user_groups(user)

    ## CUD ##

    def create(self, data):
        principal = self._principal_service.create({
            'id': data['id'],
            'type': 'group'
        })
        group = Group(
            principal.id
        )
        return self._group_store.create(group)

    def update(self, data):
        group = Group(
            data['id']
        )
        return self._group_store.update(group)

    def delete(self, group_id):
        group = Group(
            group_id
        )
        self._group_store.delete(group)
        self._principal_service.delete(group_id)


def bootstrap(app):
    app.register_factory(GroupService)
