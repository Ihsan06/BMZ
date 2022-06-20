from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("new_country", views.new_country, name="new_country"),
    path("new_project", views.new_project, name="new_project"),
    path("country_management", views.country_management, name="country_management"),
    path("change_country", views.change_country, name="change_country"),
    path("change_project", views.change_project, name="change_project"),
]
