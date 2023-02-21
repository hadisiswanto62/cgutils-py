from rest_framework import serializers

class CharacterSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    name_kana = serializers.CharField()