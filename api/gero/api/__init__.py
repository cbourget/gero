import falcon

from capri.falcon.request import create_http_request_factory

from gero.app.contexts.api import ApiContext as IApiContext
from gero.api.context import ApiContext
from gero.api.response import HttpResponse, HttpResponseProcessor
from gero.api.resource import RootResource


def create_api(app):
    request_factory = create_http_request_factory(ApiContext, IApiContext)
    api = falcon.API(
        request_type=request_factory(app),
        response_type=HttpResponse,
        middleware=[HttpResponseProcessor()])

    app.include('.auth', api)

    api.add_route('/', RootResource())

    return api
