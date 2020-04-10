from sqlalchemy.sql import select

from capri.alchemy.database import Database

from gero.app.domain.user.model import User
from gero.app.domain.user.store import UserStore


class DatabaseUserStore(UserStore):

    def __init__(self, database, user_table):
        self._database = database
        self._user_table = user_table

    def one_by_id(self, user_id):
        query = select([
            self._user_table
        ]).where(self._user_table.c.id == user_id)
        row = self._database.execute(query).first()

        if row:
            return User(row.id)
        return None

    def create(self, user):
        row = {'id': user.id}
        insert = self._user_table.insert().values(**row)
        self._database.execute(insert)

        return user

    def update(self, user):
        row = {'id': user.id}
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


def database_user_store_factory(context):
    database = context.get_instance(Database)
    user_table_name = context.settings.get('database.tables.user', 'users')
    user_table = database.metadata.tables[user_table_name]
    return DatabaseUserStore(database, user_table)


def bootstrap(app):
    app.register_factory(database_user_store_factory, UserStore)
