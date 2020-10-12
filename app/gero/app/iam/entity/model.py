class Entity:

    def __init__(self, id, type):
        self.id = id
        self.type = type

    def dump(self):
        return {
            'id': self.id,
            'type': self.type
        }


class EntityProxy:

    def __init__(self, obj, actions):
        self.obj = obj
        self.actions = actions

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def __bool__(self):
        return self.obj is not None

    def __iter__(self):
        return iter([self.obj, self.actions])

    def dump(self):
        data = self.obj.dump()
        data.update({
            '__actions': self.actions
        })
        return data