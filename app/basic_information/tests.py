# Create your tests here.

from django.test import TestCase
from .models import User, Category, Question


class QuestionModelTest(TestCase):

    def setUp(self):
        # テスト用のユーザーを作成
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword",
            first_name="Test",
            last_name="User",
            email="test@example.com",
        )
        # テスト用のカテゴリを作成
        self.category = Category.objects.create(name="Test Category", level=1)
        # テスト用の問題を作成
        self.Question = Question.objects.create(
            title="Test Question",
            content="This is a test Question.",
            category=self.category,
            option_1="Option 1",
            option_2="Option 2",
            option_3="Option 3",
            option_4="Option 4",
            is_latest=True,
        )

    def test_Question_creation(self):
        """問題が正しく作成されるかどうかをテスト"""
        self.assertEqual(self.Question.title, "Test Question")
        self.assertEqual(self.Question.content, "This is a test Question.")
        self.assertEqual(self.Question.category, self.category)

    def test_user_creation(self):
        """ユーザーが正しく作成されるかどうかをテスト"""
        self.assertEqual(self.user.username, "testuser")
        self.assertEqual(self.user.email, "test@example.com")

    def test_Question_retrieval(self):
        """問題が正しく取得できるかどうかをテスト"""
        Questions = Question.objects.all()
        self.assertEqual(len(Questions), 1)
        self.assertEqual(Questions[0], self.Question)

    def test_category_retrieval(self):
        """カテゴリが正しく取得できるかどうかをテスト"""
        categories = Category.objects.all()
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0], self.category)


from django.shortcuts import render
from .models import Question


def project_list(request):
    Questions = Question.objects.all()  # 変数名を修正
    return render(
        request, "Question_list.html", {"Questions": Questions}
    )  # キー名を修正
