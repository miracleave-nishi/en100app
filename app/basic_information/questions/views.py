from django.views.generic.edit import CreateView
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import JsonResponse
from basic_information.questions.models import Question, Answer
from basic_information.questions.forms import QuestionForm


class QuestionListView(TemplateView):
    template_name = "questions/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["questions"] = Question.objects.all()
        context["results"] = []
        return context

    def post(self, request, *args, **kwargs):
        # 個別の問題回答処理
        question_id = request.POST.get("question_id")
        user_answer = request.POST.get("user_answer")

        if question_id and user_answer:
            try:
                question = Question.objects.get(id=question_id)
                is_correct = user_answer == str(question.correct_option)

                # 結果を返す
                result = {
                    "question_id": question.id,
                    "is_correct": is_correct,
                    "correct_answer": question.correct_option,
                    "explanation": question.explanation,
                    "user_answer": user_answer,
                }

                return JsonResponse(result)
            except Question.DoesNotExist:
                return JsonResponse({"error": "問題が見つかりません"}, status=404)

        # 従来の全問題一括処理（フォールバック）
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


class QuestionResultView(TemplateView):
    template_name = "questions/result/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # セッションから結果データを取得
        session_results = self.request.session.get("question_results", [])

        if not session_results:
            # 結果がない場合は問題一覧にリダイレクト
            from django.shortcuts import redirect

            return redirect("question")

        # 結果データを整形
        questions = Question.objects.filter(
            id__in=[r["question_id"] for r in session_results]
        )
        results = []

        for result_data in session_results:
            question = questions.filter(id=result_data["question_id"]).first()
            if question:
                results.append(
                    {
                        "question": question,
                        "user_answer": result_data["user_answer"],
                        "is_correct": result_data["is_correct"],
                        "correct_answer": result_data["correct_answer"],
                        "explanation": result_data["explanation"],
                    }
                )

        # 統計情報を計算
        total_questions = len(results)
        correct_answers = sum(1 for r in results if r["is_correct"])
        incorrect_answers = total_questions - correct_answers
        accuracy_rate = (
            (correct_answers / total_questions * 100) if total_questions > 0 else 0
        )

        context.update(
            {
                "results": results,
                "total_questions": total_questions,
                "correct_answers": correct_answers,
                "incorrect_answers": incorrect_answers,
                "accuracy_rate": round(accuracy_rate, 1),
            }
        )

        return context

    def post(self, request, *args, **kwargs):
        import json

        try:
            # JSONデータを取得
            data = json.loads(request.body)
            results = data.get("results", [])

            # セッションに結果を保存
            request.session["question_results"] = results

            return JsonResponse({"status": "success"})
        except json.JSONDecodeError:
            return JsonResponse(
                {"status": "error", "message": "Invalid JSON"}, status=400
            )
        except Exception as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=500)


class QuestionCreateView(LoginRequiredMixin, TemplateView):
    template_name = "questions/create/index.html"
    success_url = reverse_lazy("question_create")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = QuestionForm()
        return context

    def post(self, request, *args, **kwargs):
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user  # 作成者を設定
            question.save()

            messages.success(
                request, f"問題「{question.title}」が正常に登録されました。"
            )

            # 成功時は空フォームを表示
            context = self.get_context_data(**kwargs)
            context["form"] = QuestionForm()
            return self.render_to_response(context)
        else:
            context = self.get_context_data(**kwargs)
            context["form"] = form
            return self.render_to_response(context)
