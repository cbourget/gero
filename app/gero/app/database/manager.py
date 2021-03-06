from sqlalchemy import (
    Column,
    Integer,
    Text,
    Table,
    ForeignKey
)

from gero.app.database import Database
from gero.app.contexts.cli import CliContext


class DatabaseManager:

    def __init__(self, database: Database):
        self._database = database
        self._mapper = database.mapper

    def initialize(self):
        with self._database.connect() as c, c.begin():
            self._create_policy_table(c)
            self._create_role_table(c)
            self._create_role_policy_table(c)
            self._create_principal_table(c)
            self._create_principal_role_table(c)
            self._create_group_table(c)
            self._create_user_table(c)
            self._create_user_group_table(c)
            self._create_entity_table(c)
            self._create_data_source_table(c)
            self._create_data_source_principal_table(c)

    def reset(self):
        keys = [
            'data_source_principal',
            'data_source',
            'entity',
            'user_group',
            'user',
            'group',
            'principal_role',
            'principal',
            'role_policy',
            'role',
            'policy'
        ]
        with self._database.connect() as c, c.begin():
            for key in keys:
                try:
                    table = self._database[key]
                except KeyError:
                    pass
                else:
                    table.drop(c) 

    def _create_policy_table(self, connection):
        table = Table(
            self._mapper['policy'],
            self._database.metadata,
            Column(
                'id',
                Integer,
                primary_key=True),
            Column(
                'name',
                Text,
                nullable=False),
            Column(
                'scope',
                Text,
                nullable=False),
            Column(
                'action',
                Text,
                nullable=False),
            Column(
                'subset',
                Text,
                nullable=False),
            Column(
                'attribution',
                Text))
        table.create(connection)

    def _create_role_table(self, connection):
        table = Table(
            self._mapper['role'],
            self._database.metadata,
            Column(
                'id',
                Integer,
                primary_key=True),
            Column(
                'name',
                Text,
                nullable=False))
        table.create(connection)

    def _create_role_policy_table(self, connection):
        table = Table(
            self._mapper['role_policy'],
            self._database.metadata,
            Column(
                'role_id',
                Integer,
                ForeignKey(
                    '{}.id'.format(self._mapper['role']),
                    ondelete='cascade'),
                primary_key=True),
            Column(
                'policy_id',
                Integer,
                ForeignKey(
                    '{}.id'.format(self._mapper['policy']),
                    ondelete='cascade'),
                primary_key=True))
        table.create(connection)

    def _create_principal_table(self, connection):
        table = Table(
            self._mapper['principal'],
            self._database.metadata,
            Column(
                'id',
                Integer,
                primary_key=True),
            Column(
                'type',
                Text,
                nullable=False))
        table.create(connection)

    def _create_principal_role_table(self, connection):
        table = Table(
            self._mapper['principal_role'],
            self._database.metadata,
            Column(
                'principal_id',
                Integer,
                ForeignKey(
                    '{}.id'.format(self._mapper['principal']),
                    ondelete='cascade'),
                primary_key=True),
            Column(
                'role_id',
                Integer,
                ForeignKey(
                    '{}.id'.format(self._mapper['role']),
                    ondelete='cascade'),
                primary_key=True))
        table.create(connection)

    def _create_group_table(self, connection):
        table = Table(
            self._mapper['group'],
            self._database.metadata,
            Column(
                'id',
                Integer,
                ForeignKey(
                    '{}.id'.format(self._mapper['principal']),
                    ondelete='cascade'),
                primary_key=True))
        table.create(connection)

    def _create_user_table(self, connection):
        table = Table(
            self._mapper['user'],
            self._database.metadata,
            Column(
                'id',
                Integer,
                ForeignKey(
                    '{}.id'.format(self._mapper['principal']),
                    ondelete='cascade'),
                primary_key=True))
        table.create(connection)

    def _create_user_group_table(self, connection):
        table = Table(
            self._mapper['user_group'],
            self._database.metadata,
            Column(
                'user_id',
                Integer,
                ForeignKey(
                    '{}.id'.format(self._mapper['user']),
                    ondelete='cascade'),
                primary_key=True),
            Column(
                'group_id',
                Integer,
                ForeignKey(
                    '{}.id'.format(self._mapper['group']),
                    ondelete='cascade'),
                primary_key=True),
            Column(
                'attribution',
                Text,
                nullable=False))
        table.create(connection)

    def _create_entity_table(self, connection):
        table = Table(
            self._mapper['entity'],
            self._database.metadata,
            Column(
                'id',
                Integer,
                primary_key=True),
            Column(
                'type',
                Text,
                nullable=False))
        table.create(connection)

    def _create_data_source_table(self, connection):
        table = Table(
            self._mapper['data_source'],
            self._database.metadata,
            Column(
                'id',
                Integer,
                primary_key=True),
            Column(
                'type',
                Text,
                nullable=False))
        table.create(connection)

    def _create_data_source_principal_table(self, connection):
        table = Table(
            self._mapper['data_source_principal'],
            self._database.metadata,
            Column(
                'data_source_id',
                Integer,
                ForeignKey(
                    '{}.id'.format(self._mapper['data_source']),
                    ondelete='cascade'),
                primary_key=True),
            Column(
                'principal_id',
                Integer,
                ForeignKey(
                    '{}.id'.format(self._mapper['principal']),
                    ondelete='cascade'),
                primary_key=True))
        table.create(connection)


def bootstrap(app):
    app.register_factory(DatabaseManager, ctx_iface=CliContext)
