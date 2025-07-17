from django.contrib import admin
from basic_information.users.models import CustomUser
from basic_information.questions.models import Category, Question, Answer
from basic_information.stamp.models import UserStamp, Stamp
from basic_information.ranking.models import Ranking

# Register your models here.

# ユーザー関連
admin.site.register(CustomUser)

# 問題関連
admin.site.register(Category)
admin.site.register(Question)
admin.site.register(Answer)

# スタンプ・ランキング関連
admin.site.register(UserStamp)
admin.site.register(Stamp)
admin.site.register(Ranking)
