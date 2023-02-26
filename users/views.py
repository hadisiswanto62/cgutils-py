from rest_framework.generics import CreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework import serializers

from cards.views import FilterableListView
from cards.models import Card
from .models import UserData, OwnedCard
from .serializers import OwnedCardSimpleSerializer, OwnedCardCreateSerializer


class UserOwnedCardListView(FilterableListView, CreateModelMixin):
    def get_serializer_class(self, *args, **kwargs):
        if self.request.method == "POST":
            return OwnedCardCreateSerializer
        return OwnedCardSimpleSerializer

    def get_queryset(self):
        return self._get_userdata().ownedcard_set.all()

    def _get_userdata(self) -> UserData:
        return UserData.objects.get(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        request.data["user_data"] = self._get_userdata().id
        return super().create(request, *args, **kwargs)
