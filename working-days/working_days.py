# # +
import calendar
import datetime
from workalendar.america import BrazilSaoPauloCity


def working_days(
    year: int = datetime.datetime.now().year, month: int = datetime.datetime.now().month
) -> int:
    cal = BrazilSaoPauloCity()
    min_day, max_day = calendar.monthrange(year, month)
    min_date = datetime.date(year, month, 1)
    max_date = datetime.date(year, month, max_day)
    working_days_nb = 0
    for day in range(1, max_day + 1):
        if cal.is_working_day(datetime.date(year, month, day)) is True:
            working_days_nb += 1
    return working_days_nb


if __name__ == "__main__":
    case1 = working_days()
    case2 = working_days(2023, 2)
    case3 = working_days(2022, 1)
    print(case1, case2, case3)
