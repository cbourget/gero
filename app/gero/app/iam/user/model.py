from gero.app.iam.principal.model import Principal


class User:

    def __init__(self, id):
        self.id = id

    @property
    def principal(self):
        return Principal(self.id, 'user')

    def dump(self):
        return {'id': self.id}
