from datetime import datetime, timedelta

# pattern = '%H:%M'
# dt = [input() for _ in range(2)]
# lst_dt = [datetime.strptime(dt[i], pattern) for i in range(len(dt))]
# #if (lst_dt[0] + timedelta(minutes=45)) < lst_dt[1]:
# while (lst_dt[0] + timedelta(minutes=45)) <= lst_dt[1]:
#     lst_dt.append(lst_dt[0] + timedelta(minutes=45))
#     print(datetime.strftime(lst_dt[0], pattern),'-', datetime.strftime(lst_dt[-1], pattern))
#     lst_dt[0] += timedelta(minutes=55)  

#a = [abs((lst_dt[i+1] - lst_dt[i+1-1]).days) for i in range(len(lst_dt)) if i < len(lst_dt)-1]
# dt = input().split()
# lst_dt = [datetime.strptime(dt[i], pattern) for i in range(len(dt))]
# a = [abs((lst_dt[i+1] - lst_dt[i+1-1]).days) for i in range(len(lst_dt)) if i < len(lst_dt)-1]
# print(lst_dt)






# h, m, s = map(int, input().split(':'))
# sec = int(input())
# sec = int(input())
# print(round(timedelta(hours=h, minutes=m, seconds=s).total_seconds()))
# dt = timedelta(hours=h, minutes=m, seconds=s+sec)
# dt = datetime.strptime(input(), '%H:%M:%S') + timedelta(seconds=int(input()))
# vr = dt + timedelta(seconds=sec) 
#vr = dt + 90
# print(dt.time())
#dt = datetime.strpdate(input(), '%d:%m:%Y')
#dt = datetime.date(input(), '%d:%m:%Y')
# pattern = '%d.%m.%Y'
# a = [abs((lst_dt[i+1] - lst_dt[i+1-1]).days) for i in range(len(lst_dt)) if i < len(lst_dt)-1]
# dt = input().split()
# lst_dt = [datetime.strptime(dt[i], pattern) for i in range(len(dt))]
# a = [abs((lst_dt[i+1] - lst_dt[i+1-1]).days) for i in range(len(lst_dt)) if i < len(lst_dt)-1]
# for i in range(len(lst_dt)):
#     if i < len(lst_dt)-1:
#         #lst_dt[i+1] - lst_dt[i+1-1]
#         a.append(abs((lst_dt[i+1] - lst_dt[i+1-1]).days))
#     else:
#         break


# for i in range(len(dt)):
#     lst_dt.append(datetime.strptime(dt[i], pattern))

# dt = datetime.strptime(input().split(), pattern)
# for i in range(2,11):
#     dt += timedelta(days=i)
#     print(dt.strftime(pattern))
# print(a)