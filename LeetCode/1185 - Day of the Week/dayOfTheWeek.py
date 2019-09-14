import datetime


dt = datetime.datetime.today()
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:

        target = datetime.date(year = year, month = month, day = day)
        days_diff = (target - dt.date()).days
        sign = 1
        if days_diff >= 0:

            idx = (dt.weekday() + days_diff) % 7
            return days[sign * idx]
        else:
            days_back = dt.weekday() + days_diff
            if days_back >= 0:
                return days[days_back]
            else:
                return days[-1 * (abs(days_back) % 7)]
