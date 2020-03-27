class User:

    def __init__(self, id):
        self.id = id

    def dump(self):
        return {'id': self.id}
