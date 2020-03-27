import jwt

from gero.api.auth.strategy import AuthStrategy


class JWTAuthStrategy(AuthStrategy):

    algorithms = [
        'HS256', 'HS384', 'HS512',
        'ES256', 'ES384', 'ES512',
        'RS256', 'RS384', 'RS512',
        'PS256', 'PS384', 'PS512'
    ]

    def __init__(self, secret, algorithm,
                 issuer=None, audience=None, leeway=0):
        super().__init__()

        self.secret = secret
        self.algorithm = algorithm
        self.issuer = issuer
        self.audience = audience
        self.leeway = leeway

    def decode_claims(self, request):
        headers = request.headers
        token = headers.get('AUTHORIZATION', '').partition('Bearer ')[2]

        try:
            claims = jwt.decode(token,
                                key=self.secret,
                                issuer=self.issuer,
                                audience=self.audience,
                                leeway=self.leeway)
        except jwt.DecodeError as err:
            claims = {}

        return claims

    def encode_claims(self, request, response, body, claims):
        token = jwt.encode(claims, self.secret, algorithm=self.algorithm)
        body['token'] = token.decode('utf-8')


def jwt_auth_strategy_factory(context):
    secret = context.settings.get('jwt.secret')
    algorithm = context.settings.get('jwt.algorithm')
    return JWTAuthStrategy(secret, algorithm)


def bootstrap(app, api):
    algorithm = app.settings.get('jwt.algorithm')
    if algorithm not in JWTAuthStrategy.algorithms:
        raise KeyError('JWT: Unsupported algorithm. Verify your settings.')

    secret = app.settings.get('jwt.secret')
    if not secret:
        raise KeyError('JWT: No secret found. Verify your settings.')


    app.register_factory(jwt_auth_strategy_factory, AuthStrategy)
