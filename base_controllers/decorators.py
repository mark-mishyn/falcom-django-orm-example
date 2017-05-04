import falcon


def authentication_required(req, resp, resource, params):
    if not req.user:
        raise falcon.HTTPUnauthorized('Authentication required',
                                      'Authentication token wasn\'t provided')
