from datetime import time, date, datetime
# import locale

# locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')
# locale.setlocale(locale.LC_ALL, 'en_EN.UTF-8')
#a = sorted([date.fromisoformat(input()) for _ in range(int(input()))])
#b = sorted(a)
#print(*[i.strftime('%d/%m/%Y') for i in sorted([date.fromisoformat(input()) for _ in range(int(input()))])], sep="\n")
#print(b)
#print(map(str,sorted(a, key=lambda x: x == x)).strftime('%d/%m/%Y'))
#a = date.fromisoformat(*[input() for _ in range(int(input()))]).strftime('%d-%m (%Y)')

# birthday = date(1992, 10, 6)

# print('Название месяца:', birthday.isoformat())
# print('Название дня недели:', birthday.strftime('%m/%d/%Y'))
# print('Год:', birthday.strftime('%Y'))
# print('Месяц:', birthday.strftime('%m'))
# print('День:', birthday.strftime('%d'))

# from datetime import date

# andrew = date(1992, 8, 24)

# print(andrew.strftime('%Y-%m'))   # выводим дату в формате YYYY-MM
# print(andrew.strftime('%B (%Y)'))   # выводим дату в формате month_name (YYYY)
# print(andrew.strftime('%Y-%j'))   # выводим дату в формате YYYY-day_number

# times_of_purchases = [datetime(2017, 10, 1, 12, 23, 25), datetime(2017, 10, 1, 15, 26, 26), 
#                       datetime(2017, 10, 1, 15, 42, 57), datetime(2017, 10, 1, 17, 49, 59), 
#                      ]
# print(len(times_of_purchases))
# a = list(filter(lambda x: x.hour > 12, times_of_purchases))
# print('До полудня' if (len(times_of_purchases) - len(a)) < len(a) else 'После полудня')

# dates = [date(2020, 11, 12), date(2021, 7, 2), date(2020, 9, 25)]
# times = [time(12, 50, 22), time(12, 19, 1), time(7, 30, 1)]
# i = 0
# a = []
# while i < len(dates):
#     a.append(datetime.combine(dates[i], times[i]))    
#     i+=1
# print(*sorted(a, key=lambda x: x.second), sep="\n")

from datetime import datetime

# data = {'Дима': ('03.11.2021 09:31:18', '03.11.2021 11:41:28'), 
#         'Геор': ('01.11.2021 09:03:04', '01.11.2021 12:40:35'), 
#         }
# b = {}
# for key, voluem in data.items():
#     b.update({key:(datetime.strptime(voluem[1],'%d.%m.%Y %H:%M:%S').timestamp() - datetime.strptime(voluem[0],'%d.%m.%Y %H:%M:%S').timestamp())})
# print(sorted(b.items(), key=lambda x: x[1])[0][0])