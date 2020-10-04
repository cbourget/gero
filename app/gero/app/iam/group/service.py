from gero.app.iam.group.model import Group
from gero.app.iam.group.store import GroupStore


class GroupService:

    def __init__(self, group_store):
        self._group_store = group_store

    ## Read ##

    def one_by_id(self, group_id):
        return self._group_store.one_by_id(group_id)

    def get_user_groups(self, user):
        return self._group_store.get_user_groups(user)

    ## CUD ##

    def create(self, data):
        group = Group(
            data['id']
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
        return self._group_store.delete(group)


def group_service_factory(context):
    group_store = context.get_instance(GroupStore)
    return GroupService(group_store)


def bootstrap(app):
    app.register_factory(group_service_factory, GroupService)
