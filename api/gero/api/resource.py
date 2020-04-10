import falcon


class RootResource:

    def on_get(self, req, resp):
        user = req.context.get_identity().user
        if user is None:
            resp.json['user'] = None
        else:
            resp.json['user'] = {
                'id': user.id
            }

        resp.status = falcon.HTTP_200
