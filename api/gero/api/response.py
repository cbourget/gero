import falcon
import json

from gero.app.utils.json import DateTimeEncoder


class HttpResponse(falcon.Response):

    def __init__(self, options=None):
        super().__init__(options=options)
        self.json = {}


class HttpResponseProcessor:

    def process_response(self, req, resp, resource, req_succeeded):
        if getattr(resp, 'body', None) is None:
            resp.body = str.encode(json.dumps(resp.json, cls=DateTimeEncoder))
