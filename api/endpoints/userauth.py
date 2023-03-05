from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.generics import CreateAPIView, ListAPIView


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = User
        fields = ("id", "username", "password")

    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data["password"])
        user.save()
        return user


class UserRegisterView(CreateAPIView):
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects
    serializer_class = UserSerializer
