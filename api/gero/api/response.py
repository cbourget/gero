import falcon
import json


class HttpResponse(falcon.Response):
    
    def __init__(self, options=None):
        super().__init__(options=options)
        self.json = {}


class HttpResponseProcessor:

    def process_response(self, req, resp, resource, req_succeeded):
        if getattr(resp, 'body', None) is None:
            resp.body = str.encode(json.dumps(resp.json, cls=DateTimeEncoder))


class DateTimeEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime):
            return o.isoformat()
        return json.JSONEncoder.default(self, o)
