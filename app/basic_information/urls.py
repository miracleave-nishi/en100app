from django.urls import path, include

urlpatterns = [
    path("", include("basic_information.home.urls"), name="home"),
    path("users/", include("basic_information.users.urls"), name="users"),
    path("questions/", include("basic_information.questions.urls"), name="questions"),
]
