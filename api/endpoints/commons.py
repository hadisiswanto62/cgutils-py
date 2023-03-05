import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination


class Page(LimitOffsetPagination):
    default_limit = 50


class FilterableListView(ListAPIView):
    pagination_class = Page
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"
