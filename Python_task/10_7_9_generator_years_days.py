from datetime import date, timedelta
from calendar import monthrange


def years_days(year: date):
    days = ((i, j) for i in range(1, 13) for j in
            range(1, monthrange(year, i)[1]+1))
    data = (date(year=year, month=i, day=j) for i, j in days)
    return data

# def years_days(year):
#     my_date = date(year, 1, 1)
#     while my_date.year == year:
#         yield my_date
#         my_date += timedelta(days=1)
