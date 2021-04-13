import falcon
from django.core.exceptions import ValidationError

from base_controllers.paginators import LimitOffsetPaginator


DEFAULT_PAGE_SIZE = 10
MAX_PAGE_SIZE = 1000


def validate_params(schema, params, partial):
    errors = schema.validate(params, partial=partial)
    if errors:
        raise falcon.HTTPBadRequest('Invalid data', errors)


def update_object(obj, params):
    for (key, value) in params.items():
        setattr(obj, key, value)

    try:
        obj.full_clean()
    except ValidationError as err:
        raise falcon.HTTPBadRequest('Invalid data', err.message_dict)

    obj.save()
    return obj


class ListMixin:
    paginator_class = LimitOffsetPaginator
    page_size = DEFAULT_PAGE_SIZE

    def get_page_size(self, req):
        page_size = req.get_param_as_int('page_size') or self.page_size
        return min(page_size, MAX_PAGE_SIZE)

    def on_get(self, req, resp):
        qs = self.get_queryset()

        if self.paginator_class:
            resp.text = self.paginator_class.get_paginated_response(
                    qs, self.get_page_size(req), req, self.schema())
        else:
            resp.text = self.schema().dumps(qs, many=True)


class CreateMixin:

    def on_post(self, req, resp):
        schema = self.schema()
        validate_params(schema, req.params, partial=False)
        new_obj = self.model()
        new_obj = update_object(new_obj, req.params)
        resp.text = schema.dumps(new_obj)


class RetrieveMixin:

    def on_get(self, req, resp, pk):
        resp.text = self.schema().dumps(self.get_object(pk))


class DestroyMixin:
    def on_delete(self, req, resp, pk):
        self.get_object(pk).delete()
        resp.status = falcon.HTTP_204


class UpdateMixin:
    def update_object(self, pk, params, resp, partial):
        schema = self.schema()
        validate_params(schema, params, partial)
        obj = self.get_object(pk)
        obj = update_object(obj, params)
        resp.text = schema.dumps(obj)

    def on_patch(self, req, resp, pk):
        self.update_object(pk, params=req.params, resp=resp, partial=True)

    def on_put(self, req, resp, pk):
        self.update_object(pk, params=req.params, resp=resp, partial=False)
