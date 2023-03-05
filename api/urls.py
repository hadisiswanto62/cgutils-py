from django.urls import path
from .endpoints.cards import ListCardView
from .endpoints.charas import ListCharactersView
from .endpoints.users import UserOwnedCardListView
from .endpoints.userauth import UserRegisterView

urlpatterns = [
    path("cards", ListCardView.as_view()),
    path("charas", ListCharactersView.as_view()),
    path("auth/register", UserRegisterView.as_view()),
    path("users/cards", UserOwnedCardListView.as_view()),
    # path("<int:chara_id>", ListCharacterCardView.as_view()),
]
