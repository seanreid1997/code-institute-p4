from . import views
from django.urls import path
from django.views import View

urlpatterns = [
    path("", views.Posts.as_view(), name="home"),
    path("register.html", views.register, name="register"),
    path("login.html", views.login, name="login"),
    path("logout.html", views.logout, name="logout"),
    path("settings.html", views.settings, name="settings"),
    path("404.html", views.page_not_found, name="404"),
    # path('<slug:slug>/', views.Posts, name='view_post'),
]
