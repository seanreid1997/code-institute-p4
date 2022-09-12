from . import views
from django.urls import path
from .views import register, login, logout

urlpatterns = [
    path("", views.Posts, name="home"),
    path("register", views.register, name="register"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout")
]
