from django.urls import path
from account.views import home_view

urlpatterns = [
    path("", home_view, name="home"),
]
