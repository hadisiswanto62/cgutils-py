import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from .models import Card
from .serializers import CardSimpleSerializer


class Page(LimitOffsetPagination):
    default_limit = 50


class FilterableListView(ListAPIView):
    pagination_class = Page
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"


class ListCardView(FilterableListView):
    queryset = Card.objects.all()
    serializer_class = CardSimpleSerializer


class ListCharacterCardView(FilterableListView):
    serializer_class = CardSimpleSerializer

    def get_queryset(self):
        char_id = self.kwargs["chara_id"]
        return Card.objects.filter(character__id=char_id).all()
