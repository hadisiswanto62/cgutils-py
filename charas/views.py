from rest_framework.generics import ListAPIView

from .models import Character
from .serializers import CharacterSerializer

class ListCharactersView(ListAPIView):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer