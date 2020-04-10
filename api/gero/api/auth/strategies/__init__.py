def bootstrap(app, api):
    strategies = {
        'jwt': '.jwt'
    }
    strategy = app.settings.get('auth.strategy')
    app.include(strategies.get(strategy, '.default'), api)
