from django.shortcuts import render
from django.http.response import HttpResponse


def home_view(request):
    return HttpResponse("this is home page")


