ANY_SCOPE = ANY_ACTION = '*'


class Identity:

    def __init__(self, user, groups, roles, policies):
        self.user = user
        self.groups = groups
        self.roles = roles
        self.policies = policies

    @property
    def principals(self):
        return [p.principal for p in [self.user] + self.groups]

    @property
    def permissions(self):
        return [p.permission for p in self.policies]


class Permission:

    def __init__(self, scope, action):
        self.scope = scope
        self.action = action

    def __str__(self):
        return '{}.{}'.format(self.scope, self.action)

    @classmethod
    def from_string(cls, string):
        scope, action = string.split('.')
        return Permission(scope=scope, action=action)

    @property
    def matching(self):
        return [
            self,
            Permission(scope=ANY_SCOPE, action=self.action),
            Permission(scope=self.scope, action=ANY_ACTION),
            Permission(scope=ANY_SCOPE, action=ANY_ACTION)
        ]
