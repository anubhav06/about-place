from functools import partial
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("newpage", views.newPage, name="newpage"),
    path("<str:country>/", views.country_page, name="country_page"),
]