from django.urls import path

from .views import UserOwnedCardListView

urlpatterns = [
    path("cards", UserOwnedCardListView.as_view()),
]
