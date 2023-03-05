from rest_framework.generics import ListAPIView
from rest_framework import serializers
from charas.models import Character


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ["id", "name", "name_kana"]


class ListCharactersView(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
