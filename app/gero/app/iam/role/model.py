class Role:

    def __init__(self, id, name):
        self.id = id
        self.name = name

    def dump(self):
        return {
            'id': self.id,
            'name': self.name
        }
