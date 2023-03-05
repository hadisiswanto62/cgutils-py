from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http.request import HttpRequest


def login_view(request: HttpRequest):
    if request.method == "POST":
        return _do_login(request)
    else:
        return _login_page(request)


def _do_login(request: HttpRequest):
    username = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect("home")


def _login_page(request):
    return render(request, "userauth/login.html")
