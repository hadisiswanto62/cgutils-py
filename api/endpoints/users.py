from collections import OrderedDict

from rest_framework import serializers, permissions
from rest_framework.mixins import CreateModelMixin

from .commons import FilterableListView
from users.models import UserData
from cards.models import Card

class OwnedCardSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card

# class OwnedCardCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = OwnedCard
#         exclude = ["id"]

#     def validate(self, data: OrderedDict):
#         if "card" in data:
#             if "level" not in data:
#                 data["level"] = data["card"].get_max_level()
#             if "skill_level" not in data:
#                 data["skill_level"] = 10
#         return super().validate(data)

class UserOwnedCardListView(FilterableListView, CreateModelMixin):
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self, *args, **kwargs):
        # if self.request.method == "POST":
        #     return OwnedCardCreateSerializer
        return OwnedCardSimpleSerializer

    def get_queryset(self):
        return self._get_userdata().cards.all()

    def _get_userdata(self) -> UserData:
        return UserData.objects.get(user=self.request.user)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        request.data["user_data"] = self._get_userdata().id
        return super().create(request, *args, **kwargs)
