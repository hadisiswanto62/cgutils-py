from django.urls import path

from .views import UserOwnedCardListView, TeamView

urlpatterns = [
    path("cards", UserOwnedCardListView.as_view(), name="add_ownedcard"),
    path("team", TeamView.as_view()),
]
