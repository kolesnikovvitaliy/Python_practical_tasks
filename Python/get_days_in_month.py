from datetime import date, timedelta
import calendar


def get_all_mondays(year):
    mondays = []
    for month in range(1, 13):
        for week in calendar.monthcalendar(year, month):
            monday = week[0]
            if monday:
                mondays.append(date(year, month, monday))
    return mondays











# def get_all_mondays(y):
#     n = [date(y, 1, 1),date(y, 12, 31)]
#     b = []
#     while n[1] >= n[0]:
#         if n[0].weekday() == 0:
#             b.append(n[0])
#             n[0] += timedelta(days=6)
#         else:
#             n[0] += timedelta(days=1)
#     return sorted(b)
# #         

# for i in range(len(b)):
#     print(b[i])    

# def get_days_in_month(y, m):
#     n = datetime(y, list(calendar.month_name).index(m),1)  
#     return [date.fromordinal(i) for i in range(n.toordinal(), n.toordinal()+(calendar.monthrange(int(y), list(calendar.month_name).index(m))[1]))]
    
# # y, m = input().split()
# # calendar.monthrange(int(y), list(calendar.month_name).index(m))[1]
# get_days_in_month(2021, 'December')
print(print(get_all_mondays(1353)))