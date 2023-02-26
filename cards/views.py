import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import ListAPIView
from rest_framework.pagination import LimitOffsetPagination, PageNumberPagination

from .models import Card
from .serializers import CardSimpleSerializer


class Page(LimitOffsetPagination):
    default_limit = 50


class ListCardView(ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSimpleSerializer
    pagination_class = Page
    filter_backends = [DjangoFilterBackend]
    filterset_fields = "__all__"


class ListCharacterCardView(ListCardView):
    serializer_class = CardSimpleSerializer
    pagination_class = Page

    def get_queryset(self):
        char_id = self.kwargs["chara_id"]
        return Card.objects.filter(character__id=char_id).all()
