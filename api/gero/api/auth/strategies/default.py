from gero.api.auth.strategy import AuthStrategy


class DefaultAuthStrategy(AuthStrategy):

    def decode_claims(self, request):
        return {'user_id': 1}

    def encode_claims(self, request, response, body, claims):
        pass


def bootstrap(app, api):
    def _default_factory(context):
        return DefaultAuthStrategy()
    app.register_factory(_default_factory, AuthStrategy)
