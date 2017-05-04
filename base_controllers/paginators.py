from ujson import dumps


class LimitOffsetPaginator:

    @staticmethod
    def get_paginated_response(queryset, page_size, req, schema):
        from app import DEFAULT_PAGE_SIZE

        page_num = req.get_param_as_int('page') or 1
        limit, offset = (page_num - 1) * page_size, page_num * page_size

        return dumps({
                'objects_count': queryset.count(),
                'page_size': DEFAULT_PAGE_SIZE,
                'data': schema.dump(queryset[limit:offset], many=True).data,
            })
