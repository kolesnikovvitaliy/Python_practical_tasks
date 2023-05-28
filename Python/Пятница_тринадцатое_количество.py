from datetime import date, time, datetime, timedelta

a = [datetime.strptime('01.01.0001', '%d.%m.%Y'),datetime.strptime('31.12.9999', '%d.%m.%Y')]
b = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}

while a[1] > a[0]:
    a[0] += timedelta(days=1)
    if a[0].day == 13:
        b[a[0].weekday()] += 1
        if a[0].year != 9999 and a[0].month != 12:
            a[0] += timedelta(days=27)

for i in range(len(b)):
    print(b[i])    

    











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
