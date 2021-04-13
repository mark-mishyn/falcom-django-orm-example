from django.core.wsgi import get_wsgi_application
import falcon

get_wsgi_application()

from middlewares import TokenAuthenticationMiddleware
from controllers import ExampleUserListResource, ExampleUserSingleResource


api = falcon.App(middleware=TokenAuthenticationMiddleware())

# TODO check if there is a way to set these settings in more elegant way
api.req_options = falcon.RequestOptions()
api.req_options.auto_parse_form_urlencoded = True

# Example controllers
api.add_route('/users/', ExampleUserListResource())
api.add_route('/users/{pk}/', ExampleUserSingleResource())

