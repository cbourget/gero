class Policy:

    def __init__(self, id, name, scope, action, subset, attribution):
        self.id = id
        self.name = name
        self.scope = scope
        self.action = action
        self.subset = subset
        self.attribution = attribution

    def dump(self):
        return {
            'id': self.id,
            'name': self.name,
            'scope': self.scope,
            'action': self.action,
            'subset': self.subset,
            'attribution': self.attribution
        }
