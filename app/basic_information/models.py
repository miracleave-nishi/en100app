from django.db import models
from basic_information.users.models import CustomUser


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
