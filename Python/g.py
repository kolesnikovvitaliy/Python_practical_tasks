import csv
import time
import datetime

aaaa = time.monotonic()
format_date = '%d/%m/%Y %H:%M'
a = dict()
c = []
with open('name_log.csv', 'r' ,encoding="utf-8") as file_in:
    rows = list(csv.reader(file_in, delimiter=","))
    b = rows[0]
    [a.setdefault(i[1], []).append([i[0], datetime.datetime.strptime(i[2], format_date)]) for i in rows[1:]]
    for i in sorted(a):
        lst = sorted(a[i],key=lambda x: x[1],reverse=True)
        c.append([lst[0][0],i, datetime.datetime.strftime(lst[0][1], format_date)])      
with open('new_name_log.csv', 'w' ,encoding="utf-8", newline='') as file_onn: 
    writer = csv.writer(file_onn)
    writer.writerow(b)
    writer.writerows(c)
# with open('name_log.csv', encoding='UTF-8') as f:
# 	header, *rows = csv.reader(f)

# d = {i[1]:i for i in sorted(rows, key=lambda x: datetime.strptime(x[2], '%d/%m/%Y %H:%M'))}

# with open('new_name_log.csv', 'w', encoding='UTF-8', newline='') as f:
# 	w = csv.writer(f)
# 	w.writerow(header)
# 	w.writerows(sorted(d.values(), key=lambda x: x[1]))
#print(b)
   # for i in c:

#     writer = csv.writer(file_onn)
#     writer.writerow(columns)
#     writer.writerows(result)       
    #print(*i, sep=',')
#     # for i in sorted(a, key=lambda x:(a[x].split('. ')[0]), reverse=True):
#     #     print(f'{i}')
# [print(i) for i in sorted(a, key=lambda x:(a[x].split('. ')[0]), reverse=True)]



bbbb = time.monotonic()
print(bbbb-aaaa)
######################################################################################
# a = dict()
# with open('titanic.csv', 'r' ,encoding="utf-8") as file:
#     rows = list(csv.reader(file, delimiter=";"))

#     for i in rows[1:]:
#         if int(i[0]) == 1 and float(i[3]) < 18:
#             a.setdefault(i[1], i[2])

#     # for i in sorted(a, key=lambda x:(a[x].split('. ')[0]), reverse=True):
#     #     print(f'{i}')
# [print(i) for i in sorted(a, key=lambda x:(a[x].split('. ')[0]), reverse=True)]
########################################################################################


    # for i in rows[1:]:
    #     a[i[1]] = a.get(i[1], 0) + int(i[-1])
    # result = sorted(sorted([[i, a[i]] for i in a], key=lambda x: x[0]), key=lambda y: int(y[1]), reverse=True)
    
    # for i in range(len(result)):
    #     print(f'{result[i][0]}: {result[i][1]}')





# bbbb = time.monotonic()
# print(bbbb-aaaa)