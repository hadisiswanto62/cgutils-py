from django.urls import path

from .views import UserRegisterView, UserListView

urlpatterns = [
    path("", UserListView.as_view()),
    path("register", UserRegisterView.as_view()),
]
