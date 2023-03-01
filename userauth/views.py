from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView

from .serializers import UserSerializer


class UserRegisterView(CreateAPIView):
    serializer_class = UserSerializer


class UserListView(ListAPIView):
    queryset = User.objects
    serializer_class = UserSerializer
