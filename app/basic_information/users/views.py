from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import CustomUserCreationForm


# Create your views here.
def login(request):
    return render(request, "users/login/index.html")


class LoginView(LoginView):
    feild = "__all__"
    template_name = "users/login/index.html"

    def get_success_url(self):
        return reverse_lazy("home")


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")  # ログインページ等、リダイレクト先を指定
    template_name = "users/signup/index.html"
