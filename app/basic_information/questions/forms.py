from django import forms
from basic_information.questions.models import Question


class QuestionForm(forms.ModelForm):
    correct_answer = forms.ChoiceField(
        choices=[
            ("1", "選択肢1 (ア)"),
            ("2", "選択肢2 (イ)"),
            ("3", "選択肢3 (ウ)"),
            ("4", "選択肢4 (エ)"),
        ],
        widget=forms.HiddenInput,  # 非表示フィールドとして設定
        required=True,
    )

    class Meta:
        model = Question
        fields = [
            "title",
            "content",
            "category",
            "option_1",
            "option_2",
            "option_3",
            "option_4",
        ]
        widgets = {
            "title": forms.TextInput(attrs={"placeholder": "問題タイトル"}),
            "content": forms.Textarea(attrs={"placeholder": "問題内容"}),
            "category": forms.Select(),
            "option_1": forms.TextInput(attrs={"placeholder": "選択肢A"}),
            "option_2": forms.TextInput(attrs={"placeholder": "選択肢B"}),
            "option_3": forms.TextInput(attrs={"placeholder": "選択肢C"}),
            "option_4": forms.TextInput(attrs={"placeholder": "選択肢D"}),
        }

    def save(self, commit=True):
        question = super().save(commit=False)
        question.correct_option = int(self.cleaned_data["correct_answer"])
        if commit:
            question.save()
        return question
