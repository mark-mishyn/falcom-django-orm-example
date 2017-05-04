from django.core.wsgi import get_wsgi_application

get_wsgi_application()

import falcon

from middlewares import TokenAuthenticationMiddleware
from controllers import ExampleUserListResource, ExampleUserSingleResource


api = falcon.API(middleware=TokenAuthenticationMiddleware())

# TODO check if there is a way to set these settings in more elegant way
api.req_options = falcon.RequestOptions()
api.req_options.auto_parse_form_urlencoded = True

# Example controllers
api.add_route('/users/', ExampleUserListResource())
api.add_route('/users/{pk}/', ExampleUserSingleResource())

DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 1000
