from django.shortcuts import render, redirect
from django.http.request import HttpRequest


# Create your views here.
def main(request: HttpRequest):
    return render(request, "home.html")
