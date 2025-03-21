from django.urls import path
from account.views import home_view, download_file, register_user

urlpatterns = [
    path("", home_view, name="home"),
    path("cookies/", download_file, name="downloadfile"),
    path("register/", register_user, name="register"),
]
