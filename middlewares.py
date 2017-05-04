import json

import falcon

from db.models import AuthToken


class JSONResponseMiddleware:

    # from https://falcon.readthedocs.io/en/stable/user/quickstart.html#learning-by-example
    def process_request(self, req, resp):

        if req.content_length in (None, 0):
            return

        body = req.stream.read()
        if not body:
            raise falcon.HTTPBadRequest('Empty request body',
                                        'A valid JSON document is required.')

        try:
            req.context['doc'] = json.loads(body.decode('utf-8'))

        except (ValueError, UnicodeDecodeError):
            raise falcon.HTTPError(falcon.HTTP_753,
                                   'Malformed JSON',
                                   'Could not decode the request body. The '
                                   'JSON was incorrect or not encoded as '
                                   'UTF-8.')


class TokenAuthentication:

    ERROR_PARAMS = {
        'title': 'Invalid authentication',
        'description': 'Header \'Authorization\' was provided, but value is invalid',
    }

    def process_request(self, req, resp):
        req.user = None
        auth_token_header = req.get_header('Authorization')

        if auth_token_header is None:
            return

        try:
            auth_type, auth_token = auth_token_header.split()
        except ValueError:
            raise falcon.HTTPBadRequest(**self.ERROR_PARAMS)

        if auth_type.lower() != 'token':
            raise falcon.HTTPBadRequest(**self.ERROR_PARAMS)

        try:
            token_obj = AuthToken.objects.get(key=auth_token)
            req.user = token_obj.user
        except AuthToken.DoesNotExist:
            raise falcon.HTTPBadRequest(**self.ERROR_PARAMS)
