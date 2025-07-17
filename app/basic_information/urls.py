from django.urls import path, include
from .views import test, mypage, QuestionCreateView
from .views import question_view
from basic_information.users.views import SignUpView

urlpatterns = [
    path("", mypage, name="mypage"),
    path("test/", test, name="test"),
    path("users/", include("basic_information.users.urls"), name="users"),
    path("question/", question_view, name="question"),
    path("question/create/", QuestionCreateView.as_view(), name="question_create"),
]
