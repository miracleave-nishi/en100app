from django.urls import path
from .views import LoginView, SignUpView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout", LogoutView.as_view(next_page="login"), name="logout"),
    path("signup/", SignUpView.as_view(), name="signup"),
]
