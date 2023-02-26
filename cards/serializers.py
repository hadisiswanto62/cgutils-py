from rest_framework import serializers
from .models import Card


class CardSimpleSerializer(serializers.ModelSerializer):
    skill = serializers.SlugRelatedField(slug_field="skill_type", read_only=True)
    leader_skill = serializers.SlugRelatedField(slug_field="name", read_only=True)

    class Meta:
        model = Card
        fields = [
            "id",
            "name",
            "character",
            "rarity",
            "attribute",
            "skill",
            "leader_skill",
            "is_evolved",
            "img_url",
        ]
