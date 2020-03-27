import falcon
import json

from gero.api.auth.service import AuthService
from gero.api.auth.validation import validate_login, validate_password
from gero.api.validation import ValidationError


class AuthSigninResource:

    def on_post(self, req, resp):
        errors = []
        payload = req.media

        try:
            login = validate_login(payload.get('login'))
        except ValidationError as err:
            errors.append(err.dump())

        try:
            password = validate_password(payload.get('password'))
        except ValidationError as err:
            errors.append(err.dump())

        if errors:
            status = falcon.HTTP_422
            resp.json['errors'] = errors
            return

        auth_service = req.context.get_instance(AuthService)
        auth_service.signin(req, resp, resp.json, login, password)

        status = falcon.HTTP_200
        resp.json['message'] = 'Hello!'
