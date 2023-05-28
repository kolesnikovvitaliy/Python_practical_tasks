from datetime import date, time, datetime, timedelta
pattern = '%d.%m.%Y'
c = {}
n = datetime.strptime(input(), pattern)
a = [input() for _ in range(int(input()))]
na = [date.fromordinal(i) for i in range(n.toordinal()+1, n.toordinal()+8)]

lst = {}
[lst.setdefault(datetime.strptime(a[i][-10:], pattern), []).append(a[i][:-10].strip()) for i in range(len(a))]
#for i in sorted(lst, key=lambda x: x.year):
for i in lst:
    if i.day in [i.day for i in na] and i.month in [i.month for i in na]:
        c.setdefault(i, lst[i])
if len(c) == 0:
    print('Дни рождения не планируются')
else:
    print(*c[max(c)])
    
# if min(lst).month == na[1] and min(lst).day in na[0]:
#     print(*lst[min(lst)])
# # for i in max(lst):
#     print(i)
#     if max(lst) in na:
#         print(max(lst))
#         print(datetime.strftime(max(lst), pattern))
# count = 0 
# for i in sorted(lst):
#     if len(lst[i]) > 1:
#         print(datetime.strftime(i, pattern))
#         count += 1

# if count == 0:
#     for i in sorted(lst):
#         print(datetime.strftime(i, pattern))

#else:
    #print(datetime.strftime(min(lst), pattern), *lst[min(lst)])
#print(len(lst[min(lst)]))





# 14.11.2021
# 3
# Иван Петров 16.11.1995
# Петр Сергеев 14.11.1997
# Сергей Романов 17.11.1994
# Sample Output 1:

# Иван Петров











# lst = {}
# [lst.setdefault(datetime.strptime(a[i][-10:], pattern), []).append(a[i][:-10].strip()) for i in range(len(a))]

# if len(lst[min(lst)]) > 1:
#     print(datetime.strftime(min(lst), pattern), len(lst[min(lst)]))
# else:
#     print(datetime.strftime(min(lst), pattern), *lst[min(lst)])
# print(len(lst[min(lst)]))
# for key, voluem in min(lst):
#     print(i)
#     if len(voluem) > 1:
#         print(datetime.strftime(key, pattern), len(voluem))
#     else:
#         print(datetime.strftime(key, pattern), voluem)

# # print(b)
# mydict[key] = mydict.get(key, []) + [value]

# date1, date2 = datetime.strptime(a[0], pattern), datetime.strptime(a[1], pattern)
# dt = [date.fromordinal(i) for i in range(date1.toordinal(), date2.toordinal()+1)]

# i = 0
# while ((dt[i].day + dt[i].month) % 2) == 0:
#     i += 1

# while (i) < len(dt):
#     if  dt[i].weekday() not in  [0, 3]:
#         print(dt[i].strftime(pattern))
#         i += 3
#     else:
#         i += 3


# 3
# Иван Петров 01.05.1995
# Петр Сергеев 29.04.1995
# Сергей Иванов 01.01.1996
# Sample Output 1:

# 29.04.1995 Петр Сергеев













# a = [input() for _ in range(2)]
# pattern = '%d.%m.%Y'
# date1, date2 = datetime.strptime(a[0], pattern), datetime.strptime(a[1], pattern)
# dt = [date.fromordinal(i) for i in range(date1.toordinal(), date2.toordinal()+1)]

# i = 0
# while ((dt[i].day + dt[i].month) % 2) == 0:
#     i += 1

# while (i) < len(dt):
#     if  dt[i].weekday() not in  [0, 3]:
#         print(dt[i].strftime(pattern))
#         i += 3
#     else:
#         i += 3

# from datetime import datetime, timedelta

# begin = datetime.strptime(input(), '%d.%m.%Y')
# end = datetime.strptime(input(), '%d.%m.%Y')

# while (begin.day + begin.month) % 2 == 0:
#     begin += timedelta(days=1)

# while begin <= end:
#     if begin.weekday() != 0 and begin.weekday() != 3:
#         print(begin.strftime('%d.%m.%Y'))
#     begin += timedelta(days=3)










# pattern = '%d.%m.%Y %H:%M'
# dt = (
#     (timedelta(hours=9), timedelta(hours=21)),
#     (timedelta(hours=9), timedelta(hours=21)),
#     (timedelta(hours=9), timedelta(hours=21)),
#     (timedelta(hours=9), timedelta(hours=21)),
#     (timedelta(hours=9), timedelta(hours=21)),
#     (timedelta(hours=10), timedelta(hours=18)),
#     (timedelta(hours=10), timedelta(hours=18))
# )
# lst_dt = datetime.strptime(input(), pattern)
# dw = lst_dt.weekday()
# h, m, s = map(int, str(lst_dt.time()).split(':'))
# rez = timedelta( hours=h, minutes=m, seconds=s)

# if rez < dt[dw][1] and rez >= dt[dw][0]:
    
    
#     if (dt[dw][1] - rez) <= dt[dw][1]:
#         print((dt[dw][1] - rez).seconds // 60)
# else:
#     print('Магазин не работает')
# #if (lst_dt[0] + timedelta(minutes=45)) < lst_dt[1]:
# while (lst_dt[0] + timedelta(minutes=45)) <= lst_dt[1]:
#     lst_dt.append(lst_dt[0] + timedelta(minutes=45))
#     print(datetime.strftime(lst_dt[0], pattern),'-', datetime.strftime(lst_dt[-1], pattern))
#     lst_dt[0] += timedelta(minutes=55)  












 a = [datetime.strptime('01.01.0001', '%d.%m.%Y'),datetime.strptime('31.12.9999', '%d.%m.%Y')]
# b = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

# while a[1] > a[0]:
#     a[0] += timedelta(days=1)
#     if a[0].day == 13:
#         b[a[0].weekday()] += 1
#         if a[0].year != 9999 and a[0].month != 12:
#             a[0] += timedelta(days=27)

# for i in range(len(b)):
#     print(b[i])    
#

    











#Программа должна вывести 77 чисел — количество тринадцатых чисел, которые приходятся на понедельник, 
# вторник, среду, четверг, пятницу, субботу и воскресенье в период с 01.01.0001 по 31.12.9999. 
# Числа должны быть расположены каждое на отдельной строке
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
# pattern = '%H:%M'
# b = datetime.strptime('00:00', pattern)
# a = [datetime.strptime(i[1], pattern) - datetime.strptime(i[0], pattern) for i in data]
# for i in a:
#     b += i 
# print((timedelta(minutes=b.minute, hours=b.hour).seconds // 60))
