from collections import OrderedDict
from rest_framework import serializers

from .models import OwnedCard


class OwnedCardSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = OwnedCard
        exclude = ["id", "user_data"]


class OwnedCardCreateSerializer(serializers.ModelSerializer):
    level = serializers.IntegerField(required=False)
    skill_level = serializers.IntegerField(required=False)

    class Meta:
        model = OwnedCard
        exclude = ["id"]

    def validate(self, data: OrderedDict):
        if "card" in data:
            if "level" not in data:
                data["level"] = data["card"].get_max_level()
            if "skill_level" not in data:
                data["skill_level"] = 10
        return super().validate(data)
