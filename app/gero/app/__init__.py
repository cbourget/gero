from capri.core.app import App


DEFAULT_TABLES_NAMES = {
    'policy': 'policies',
    'role': 'roles',
    'role_policy': 'roles_policies',
    'principal': 'principals',
    'principal_role': 'principals_roles',
    'group': 'groups',
    'user': 'users',
    'user_group': 'users_groups',
    'entity': 'entities',
    'data_source': 'data_sources',
    'data_source_principal': 'data_sources_principals'
}

def create_app(extra_settings):
    app = App(dict({
        'database': {
            # 'connection': 'postgresql+psycopg2://gero:gero@database:5432/gero?client_encoding=utf8',  # NOQA
            'connection': 'postgresql+psycopg2://gero:gero@localhost:5432/gero?client_encoding=utf8',  # NOQA
            'tables': {
                **DEFAULT_TABLES_NAMES,
                **{
                    'user': 'users'
                }
            }
        }
    }, **extra_settings))
    app.include('.database')
    app.include('.iam')
    app.include('.domain')
    return app
