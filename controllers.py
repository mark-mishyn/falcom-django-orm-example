from base_controllers.controllers import SingleModelResource, ListModelResource
from db.models import ExampleUser
from db.schemas import ExampleUserSchema


class ExampleUserListResource(ListModelResource):
    schema = ExampleUserSchema
    model = ExampleUser


class ExampleUserSingleResource(SingleModelResource):
    schema = ExampleUserSchema
    model = ExampleUser
