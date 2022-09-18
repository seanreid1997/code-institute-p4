from . import views
from django.urls import path
from django.views import View
from .views import login, logout, register, page_not_found, settings

urlpatterns = [
    path("", views.Posts.as_view(), name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("settings", views.settings, name="settings"),
    path("404", views.page_not_found, name="404")
]
