from . import views
from django.urls import path
from .views import register

urlpatterns = [
    path("", views.Posts.as_view(), name="home"),
    path("register/", views.register, name="register")
]