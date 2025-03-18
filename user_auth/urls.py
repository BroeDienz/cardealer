from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.SignUp.as_view(), name="signup"),
    path("login/", views.custom_login_view, name="login"),
    path("logout/", views.logout_and_redirect, name="logout"),
    path("back_to_home/", views.back_to_home, name="back_to_home"),
]
