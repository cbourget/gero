from gero.app.iam.principal.model import Principal


class Group:

    def __init__(self, id):
        self.id = id

    @property
    def principal(self):
        return Principal(self.id, 'group')

    def dump(self):
        return {'id': self.id}


class GroupUser(Group):

    def __init__(self, id, attribution):
        super().__init__(id)
        self.attribution = attribution

    def dump(self):
        return {
            'id': self.id,
            'attribution': self.attribution
        }

