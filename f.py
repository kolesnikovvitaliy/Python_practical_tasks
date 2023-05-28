import csv
import time
aaaa = time.monotonic()
a = dict()
with open('wifi.csv', 'r' ,encoding="utf-8") as file:
    rows = list(csv.reader(file, delimiter=";"))
    for i in rows[1:]:
        a[i[1]] = a.get(i[1], 0) + int(i[-1])
    result = sorted(sorted([[i, a[i]] for i in a], key=lambda x: x[0]), key=lambda y: int(y[1]), reverse=True)
    
   
   # a = dict()
# with open('wifi.csv', 'r' ,encoding="utf-8") as file:
#     rows = list(csv.reader(file, delimiter=";"))
#     #lst = [[i[1],i[-1]] for i in rows[1:]]
#     #a.setdefault(key)
#     #result = sorted([a.get(i[1], 0) + int(i[-1]) for i in set(lst)], key=lambda x: (int(x[1]), x[0]))
#     for i in rows[1:]:
#         a[i[1]] = a.get(i[1], 0) + int(i[-1])
#     result = sorted([[i, a[i]] for i in a], key=lambda x: (int(x[1]), x[0]))
#     # for i in rows[1:]:
#     #     a.setdefault(i[1],[]).append(int(i[-1]))
#     # result = sorted([[i, sum(a[i])] for i in a], key=lambda x: (int(x[1]), x[0]))
#     for i in range(len(result)):
#         print(result[i][0], ':', result[i][1])

bbbb = time.monotonic()
print(bbbb-aaaa)







# import time
# aaaa = time.monotonic()
# columns = ['domain', 'count']
# with open('data.csv', 'r' ,encoding="utf-8") as file_in:
#     rows = list(csv.reader(file_in))
#     lst = [i[2].split('@')[1] for i in rows[1:]]
#     result = sorted([[i,lst.count(i)] for i in set(lst)], key=lambda x: (int(x[1]), x[0]))
# with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file_onn:
#     writer = csv.writer(file_onn)
#     writer.writerow(columns)
#     writer.writerows(result)
# bbbb = time.monotonic()
# print(bbbb-aaaa)





# columns = ['domain', 'count']

# with open('data.csv', 'r' ,encoding="utf-8") as file_in:
#     rows = list(csv.reader(file_in))
#     lst = [i[2].split('@')[1] for i in rows[1:]]
#     result = sorted([[i,lst.count(i)] for i in set(lst)], key=lambda x: (int(x[1]), x[0]))

# with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file_onn:
#     writer = csv.writer(file_onn)
#     writer.writerow(columns)
#     writer.writerows(result)  

#print(result, columns)
# import csv

# columns = ['first_name', 'second_name', 'class_number', 'class_letter']
# data = [['Тимур', 'Гуев', 11, 'А'], ['Руслан', 'Чаниев', 9, 'Б'], ['Артур', 'Харисов', 10, 'В']]

# with open('students.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(columns)
#     for row in data:
#         writer.writerow(row)

#print(sorted(result, key=lambda x: (lambda y: x.items(),((y[0], int(y[1]))))))
#sorted(data.items(), key=lambda x: (sum(x[1]) / len(x[1]), x[0])):
# with open('domain_usage.csv', 'w', encoding='utf-8', newline='') as file_onn:   
#     writer = csv.DictWriter(file_onn, fieldnames=colums, delimiter=',', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writeheader()
#     for row in sorted(result, key=lambda x: (int(result[x]), x)):
#         writer.writerow(row)
#print(sorted(sorted(d, key=lambda x: x[0]), key=lambda x: int(x[1])))
#writer.writerows(data)



# with open('students.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=columns, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
#     writer.writeheader()
#     for row in data:
#         writer.writerow(row)    
