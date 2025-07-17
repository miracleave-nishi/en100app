from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import QuestionForm
from django.contrib.auth.decorators import login_required
from .models import Question


def test(request):
    test_message = 'Hello! This page is "EN100_Unit page"'
    return HttpResponse(test_message)


@login_required
def mypage(request):
    return render(request, "mypage.html")


class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = "question_create.html"
    success_url = reverse_lazy("question_create")


# モデル取得テスト用
def project_list(request):
    questions = Question.objects.all()
    return render(request, "Question_list.html", {"questions": questions})


def question_view(request):
    questions = Question.objects.all()
    results = []

    if request.method == "POST":
        for question in questions:
            user_answer = request.POST.get(f"question_{question.id}")
            if user_answer:
                is_correct = user_answer == str(question.correct_option)
                results.append(
                    {
                        "question": question,
                        "is_correct": is_correct,
                    }
                )

    return render(
        request, "question_practice.html", {"questions": questions, "results": results}
    )
