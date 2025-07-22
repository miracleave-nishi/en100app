from django.urls import path
from .views import QuestionListView, QuestionCreateView, QuestionResultView

urlpatterns = [
    path("", QuestionListView.as_view(), name="question"),
    path("create/", QuestionCreateView.as_view(), name="question_create"),
    path("result/", QuestionResultView.as_view(), name="question_result"),
]
