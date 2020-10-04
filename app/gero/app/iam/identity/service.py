from gero.app.iam.identity.model import Identity
from gero.app.iam.user.service import UserService
from gero.app.iam.group.service import GroupService
from gero.app.iam.role.service import RoleService
from gero.app.iam.policy.service import PolicyService


class IdentityService:

    def __init__(self, user_service, group_service, role_service, policy_service):
        self._user_service = user_service
        self._group_service = group_service
        self._role_service = role_service
        self._policy_service = policy_service

    def get_user_identity(self, user):
        groups = self._group_service.get_user_groups(user)
        principals = [p.principal for p in [user] + groups]
        roles = self._role_service.get_principals_roles(principals)
        policies = self._policy_service.get_roles_policies(roles)
        return Identity(user, groups, roles, policies)


def identity_service_factory(context):
    user_service = context.get_instance(UserService)
    group_service = context.get_instance(GroupService)
    role_service = context.get_instance(RoleService)
    policy_service = context.get_instance(PolicyService)
    return IdentityService(
        user_service,
        group_service,
        role_service,
        policy_service)


def bootstrap(app):
    app.register_factory(identity_service_factory, IdentityService)
