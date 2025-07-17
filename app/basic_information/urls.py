from django.urls import path, include
from .views import mypage

urlpatterns = [
    path("", mypage, name="mypage"),
    path("users/", include("basic_information.users.urls"), name="users"),
    path("questions/", include("basic_information.questions.urls"), name="questions"),
]
