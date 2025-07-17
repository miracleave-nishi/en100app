from django.db import models
from django.contrib.auth.models import AbstractUser


# ユーザーテーブル
class CustomUser(AbstractUser):
    level = models.IntegerField(default=1)  # ユーザーレベル
    experience_points = models.IntegerField(default=0)  # 経験値
    profile_picture = models.URLField(blank=True, null=True)  # プロフィール画像のURL
    # profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)  # プロフィール画像
    bio = models.TextField(null=True, blank=True)  # 自己紹介
    stamps = models.IntegerField(default=0)  # スタンプ
    role = models.CharField(
        max_length=10,
        choices=[("admin", "Administrator"), ("user", "User")],
        default="user",
    )  # 管理者と識別
    correct_answers = models.IntegerField(default=0)  # 正解数
    total_answers = models.IntegerField(default=0)  # 総回答数

    def __str__(self):
        return self.username
