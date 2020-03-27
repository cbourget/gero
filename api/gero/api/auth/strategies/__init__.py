strategies = {
    'jwt': '.jwt'
}

def bootstrap(app, api):
    strategy = app.settings.get('auth.strategy')
    app.include(strategies.get(strategy, '.default'), api)
