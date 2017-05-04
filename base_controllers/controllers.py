import falcon

from base_controllers import mixins


class BaseModelResource:
    schema = None
    model = None

    def get_queryset(self):
        return self.model.objects.all()

    def get_object(self, pk):
        try:
            return self.get_queryset().get(pk=pk)
        except self.model.DoesNotExist:
            raise falcon.HTTPNotFound()


class ListModelResource(mixins.ListMixin,
                        mixins.CreateMixin,
                        BaseModelResource):
    pass


class SingleModelResource(mixins.RetrieveMixin,
                          mixins.DestroyMixin,
                          mixins.UpdateMixin,
                          BaseModelResource):
    pass
