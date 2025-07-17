from django.db import models
from basic_information.users.models import CustomUser


# カテゴリテーブル
class Category(models.Model):

    name = models.CharField(
        max_length=100, default="Default Category"
    )  # デフォルト値を指定
    parent_id = models.ForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True
    )  # 親カテゴリID

    level = models.IntegerField()  # カテゴリレベル
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日
    updated_at = models.DateTimeField(auto_now=True)  # 更新日

    def __str__(self):
        return self.name


# 問題テーブル
class Question(models.Model):
    title = models.CharField(max_length=255)  # 問題タイトル
    content = models.TextField()  # 問題内容
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # 外部キー
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日
    updated_at = models.DateTimeField(auto_now=True)  # 更新日
    option_1 = models.CharField(max_length=255)  # 選択肢1
    option_2 = models.CharField(max_length=255)  # 選択肢2
    option_3 = models.CharField(max_length=255)  # 選択肢3
    option_4 = models.CharField(max_length=255, null=True)  # 選択肢4
    correct_option = models.IntegerField(null=True)  # 正解の選択肢の追加
    explanation = models.TextField(null=True, blank=True)  # 解説

    def __str__(self):
        return self.title


# 回答テーブル
class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # 外部キー
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 外部キー
    selected_option = models.IntegerField()  # 選択したオプション
    is_correct = models.BooleanField(default=False)  # 正解かどうか
    created_at = models.DateTimeField(auto_now_add=True)  # 回答日
    is_latest = models.BooleanField(default=False)  # 最新かどうかのフラグ

    def __str__(self):
        return f"Answer by {self.user.username} for {self.Question.title}"


# ユーザースタンプテーブル
class UserStamp(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 外部キー
    stamp_id = models.IntegerField()  # スタンプID
    date = models.DateField()  # スタンプ日付
    created_at = models.DateTimeField(auto_now_add=True)  # 作成日

    def __str__(self):
        return f"Stamp for {self.user.username} on {self.date}"


# スタンプテーブル
class Stamp(models.Model):
    stamp_id = models.AutoField(primary_key=True)  # プライマリーキー
    stamp_image = models.URLField(blank=True, null=True)  # スタンプ画像

    def __str__(self):
        return f"Stamp {self.stamp_id}"


# ランキングテーブル
class Ranking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 外部キー
    score = models.IntegerField()  # スコア
    rank = models.IntegerField()  # 順位
    created_at = models.DateTimeField(auto_now_add=True)  # 記録日

    def __str__(self):
        return f"Ranking for {self.user.username} - Rank: {self.rank}"
