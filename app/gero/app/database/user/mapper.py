from sqlalchemy.sql import select

from gero.app.domain.user.model import User
from gero.app.database.mapper import DatabaseMapper


class DatabaseUserMapper(DatabaseMapper):

    def row_to_instance(self, row):
        return User(row.id)

    def instance_to_insert(self, instance):
        return {'id': instance.id}

    def instance_to_update(self, instance):
        return {'id': instance.id}


def database_user_mapper_factory(context):
    return DatabaseUserMapper()


def bootstrap(app):
    app.register_factory(database_user_mapper_factory, DatabaseUserMapper)
