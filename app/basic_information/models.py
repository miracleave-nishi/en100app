from django.db import models
from basic_information.users.models import CustomUser


# ランキングテーブル
class Ranking(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # 外部キー
    score = models.IntegerField()  # スコア
    rank = models.IntegerField()  # 順位
    created_at = models.DateTimeField(auto_now_add=True)  # 記録日

    def __str__(self):
        return f"Ranking for {self.user.username} - Rank: {self.rank}"
