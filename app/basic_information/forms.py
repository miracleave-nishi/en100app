from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Question


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ("username", "password1", "password2")  # 必要に応じてフィールド追加


class QuestionForm(forms.ModelForm):
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
