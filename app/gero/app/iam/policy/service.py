from gero.app.iam.policy.store import PolicyStore


class PolicyService:

    def __init__(self, policy_store):
        self._policy_store = policy_store

    ## Read ##

    def one_by_id(self, policy_id):
        return self._policy_store.one_by_id(policy_id)

    def get_roles_policies(self, roles):
        return self._policy_store.get_roles_policies(roles)


def policy_service_factory(context):
    policy_store = context.get_instance(PolicyStore)
    return PolicyService(policy_store)


def bootstrap(app):
    app.register_factory(policy_service_factory, PolicyService)
