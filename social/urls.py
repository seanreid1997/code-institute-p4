from . import views
from django.urls import path
from .views import register, login

urlpatterns = [
    path("", views.Posts.as_view(), name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login")
]