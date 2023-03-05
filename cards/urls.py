from django.urls import path
from .views import CardListView

urlpatterns = [
    path("", CardListView.as_view(), name="cards_list"),
]
