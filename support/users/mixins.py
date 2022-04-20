from rest_framework import mixins
from rest_framework import viewsets


class CreateListViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    """Mixin for create or get list"""
    pass
