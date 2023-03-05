from rest_framework import serializers

from .commons import FilterableListView
from cards.models import Card


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


class ListCardView(FilterableListView):
    queryset = Card.objects.all()
    serializer_class = CardSimpleSerializer


class ListCharacterCardView(FilterableListView):
    serializer_class = CardSimpleSerializer

    def get_queryset(self):
        char_id = self.kwargs["chara_id"]
        return Card.objects.filter(character__id=char_id).all()
