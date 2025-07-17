from django.urls import path, include

urlpatterns = [
    path("", include("basic_information.mypage.urls"), name="mypage"),
    path("users/", include("basic_information.users.urls"), name="users"),
    path("questions/", include("basic_information.questions.urls"), name="questions"),
]
