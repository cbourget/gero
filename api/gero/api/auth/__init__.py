from gero.api.auth.resource import AuthSigninResource

def bootstrap(app, api):
    app.include('.strategies', api)
    app.include('.service', api)

    api.add_route('/signin', AuthSigninResource())
