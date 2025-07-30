from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from datetime import date, timedelta
import calendar


class HomeView(LoginRequiredMixin, TemplateView):
    template_name = "home/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        target_date = self.get_target_date()
        year, month = target_date.year, target_date.month

        calendar_days = self.generate_calendar_days(year, month)
        prev_date, next_date = self.get_adjacent_months(target_date)

        context.update(
            {
                "current_year": year,
                "current_month": month,
                "calendar_days": calendar_days,
                "prev_year": prev_date.year,
                "prev_month": prev_date.month,
                "next_year": next_date.year,
                "next_month": next_date.month,
            }
        )
        return context

    def get_target_date(self):
        """GETパラメータから年月を取得。なければ今日"""
        year = self.request.GET.get("year")
        month = self.request.GET.get("month")
        today = date.today()

        try:
            return date(int(year), int(month), 1)
        except (TypeError, ValueError):
            return today

    def generate_calendar_days(self, year, month):
        """対象月のカレンダー表示用日付リスト（前後月含む6週分）を生成"""
        today = date.today()
        cal = calendar.Calendar(firstweekday=6)  # Sunday start
        month_days = list(cal.itermonthdates(year, month))  # 各日付を date 型で取得

        # 学習履歴などを反映する場合はここで処理を加える
        calendar_days = []
        for day in month_days:
            calendar_days.append(
                {
                    "date": day,
                    "day_number": day.day,
                    "is_current": day == today,
                    "is_other_month": day.month != month,
                    "is_studied": False,  # TODO: DB連携で処理
                }
            )
        return calendar_days

    def get_adjacent_months(self, current_date):
        """前月・翌月を返す"""
        first_day = current_date.replace(day=1)
        prev_month = (first_day - timedelta(days=1)).replace(day=1)
        next_month = (first_day + timedelta(days=31)).replace(day=1)
        return prev_month, next_month
