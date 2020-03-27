from gero.app import create_app
from gero.api import create_api

app = create_app({
    'auth': {
        'strategy': 'default'
    },
    'jwt': {
        'secret': 'foo',
        'algorithm': 'HS256'
    }
})
api = application = create_api(app)
