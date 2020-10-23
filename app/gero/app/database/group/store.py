from sqlalchemy.sql import select

from gero.app.database import Database

from gero.app.iam.group.model import Group, GroupUser
from gero.app.iam.group.store import IGroupStore


class GroupStore(IGroupStore):

    def __init__(self, database: Database):
        self._database = database
        self._group_table = database['group']
        self._user_group_table = database['user_group']

    # Mappers

    def _row_to_group(self, row):
        return Group(row.id)

    def _row_to_group_user(self, row):
        return GroupUser(row.id, row.attribution)

    def _group_to_row(self, group):
        return {
            'id': group.id
        }

    ## Read ##

    def one_by_id(self, group_id):
        query = select([
            self._group_table
        ]).where(self._group_table.c.id == group_id)
        row = self._database.execute(query).first()

        if row:
            return self._row_to_group(row)
        return None

    def get_user_groups(self, user):
        query = self._query_groups_by_user(user)

        return [
            self._row_to_group_user(row)
            for row in self._database.execute(query)
        ]

    def _query_groups_by_user(self, user):
        return select([
            self._group_table,
            self._user_group_table.c.attribution
        ]).select_from(
            self._group_table.join(
                self._user_group_table,
                self._group_table.c.id == self._user_group_table.c.group_id
            )
        ).where(
            self._user_group_table.c.user_id == user.id
        )

    ## CUD ##

    def create(self, group):
        row = self._group_to_row(group)
        insert = self._group_table.insert().values(**row)
        self._database.execute(insert)

        return group

    def update(self, group):
        row = self._group_to_row(group)
        update = self._group_table.update().where(
            self._group_table.c.id == group.id
        ).values(**row)
        self._database.execute(update)

        return group

    def delete(self, group):
        delete = self._group_table.delete().where(
            self._group_table.c.id == group.id
        )
        self._database.execute(delete)

def bootstrap(app):
    app.register_factory(GroupStore, IGroupStore)
