from sqlalchemy.sql import select

from gero.app.database import Database

from gero.app.iam.user.model import User
from gero.app.iam.user.store import IUserStore


class UserStore(IUserStore):

    def __init__(self, database: Database):
        self._database = database
        self._user_table = database['user']

    # Mappers

    def _row_to_user(self, row):
        return User(row.id)

    def _user_to_row(self, user):
        return {
            'id': user.id
        }

    ## Read ##

    def one_by_id(self, user_id):
        query = select([
            self._user_table
        ]).where(self._user_table.c.id == user_id)
        row = self._database.execute(query).first()

        if row:
            return self._row_to_user(row)
        return None

    ## CUD ##

    def create(self, user):
        row = self._user_to_row(user)
        insert = self._user_table.insert().values(**row)
        self._database.execute(insert)

        return user

    def update(self, user):
        row = self._user_to_row(user)
        update = self._user_table.update().where(
            self._user_table.c.id == user.id
        ).values(**row)
        self._database.execute(update)

        return user

    def delete(self, user):
        delete = self._user_table.delete().where(
            self._user_table.c.id == user.id
        )
        self._database.execute(delete)

def bootstrap(app):
    app.register_factory(UserStore, IUserStore)
