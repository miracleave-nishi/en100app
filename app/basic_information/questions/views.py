from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from basic_information.questions.models import Question
from basic_information.questions.forms import QuestionForm


class QuestionListView(TemplateView):
    template_name = "questions/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["questions"] = Question.objects.all()
        context["results"] = []
        return context

    def post(self, request, *args, **kwargs):
        questions = Question.objects.all()
        results = []

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

        context = self.get_context_data(**kwargs)
        context["questions"] = questions
        context["results"] = results
        return self.render_to_response(context)


class QuestionCreateView(TemplateView):
    template_name = "questions/create/index.html"
    success_url = reverse_lazy("question_create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = QuestionForm()
        return context

    def post(self, request, *args, **kwargs):
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            # 成功時は空フォーム＋完了メッセージを表示
            context = self.get_context_data(**kwargs)
            context["form"] = QuestionForm()
            context["success"] = True
            return self.render_to_response(context)
        else:
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)
