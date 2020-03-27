from capri.core.app import App


def create_app(extra_settings):
    app = App(dict({
        'database': {
            'connection': 'postgresql+psycopg2://gero:gero@localhost:5432/gero?client_encoding=utf8',
            'tables': {
                'user': 'users'
            }
        }
    }, **extra_settings))
    app.include('.database')
    app.include('.domain')
    return app
