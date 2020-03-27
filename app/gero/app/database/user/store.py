from sqlalchemy.sql import select

from capri.alchemy.database import Database

from gero.app.domain.user.model import User
from gero.app.domain.user.store import UserStore
from gero.app.database.user.mapper import DatabaseUserMapper


class DatabaseUserStore(UserStore):

    def __init__(self, database, mapper, user_table):
        self._database = database
        self._mapper = mapper
        self._user_table = user_table

    def one_by_id(self, user_id):
        query = select([
            self._user_table
        ]).where(self._user_table.c.id == user_id)
        row = self._database.execute(query).first()

        if row:
            return self._mapper.row_to_instance(row)
        return None

    def create(self, user):
        row = self._mapper.instance_to_insert(user)
        insert = self._user_table.insert().values(**row)
        self._database.execute(insert)

        return user

    def update(self, user):
        row = self._mapper.instance_to_update(user)
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
    mapper = context.get_instance(DatabaseUserMapper)
    user_table_name = context.settings.get('database.tables.user', 'users')
    user_table = database.metadata.tables[user_table_name]
    return DatabaseUserStore(database, mapper, user_table)


def bootstrap(app):
    app.register_factory(database_user_store_factory, UserStore)
