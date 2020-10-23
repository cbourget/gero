class Principal:

    def __init__(self, id, type):
        self.id = id
        self.type = type

    def dump(self):
        return {
            'id': self.id,
            'type': self.type
        }
