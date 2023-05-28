import csv

text = '''name,grade
Timur,5
Arthur,4
Anri,5'''

with open('grades.csv', 'w') as file:
    file.write(text)

import csv

def csv_columns(filename):

    with open(filename, encoding="utf-8") as file_in:
        rows = list(csv.reader(file_in))
        return {key: value for key, *value in zip(*rows)}






# import sys
# count = 0
# a = int(input())
# with open('deniro.csv', 'r', encoding='utf-8') as file:
#     rows = csv.reader(file, delimiter=',')   
#     #next(rows)
#     if a == 1:
#         for line in sorted(rows, key=lambda x: x[a-1]):
#             if count == 5:
#                 break        
#             print(*line, sep=",")
#             count += 1  
#     else:
#         for line in sorted(rows, key=lambda x: int(x[a-1])):
#             if count == 5:
#                 break
#             print(*line, sep=",")
#             count += 1  
    

    # for i in rows:
    #     a.setdefault(i[0], []).append(i[1])
    # # else:
    #     for line in sorted(rows[1:], key=lambda x: int(x[a-1])):
    #         if count == 5:
    #             break
    #         print(*line, sep=",")
    #         count += 1
      
    # print([*line] for line in sorted(sorted(a, key=lambda k: k), key=lambda x: (sum(map(int, a[x])) / len(a[x]))))
    # #b = sorted(a, key=lambda x: (sum(map(int, a[x])) / len(a[x])))
    # #b = sorted(sorted(a, key=lambda k: k), key=lambda x: (sum(map(int, a[x])) / len(a[x])))

    # for line in sorted(sorted(a, key=lambda k: k), key=lambda x: (sum(map(int, a[x])) / len(a[x]))):
    #     if count == 5:
    #         break
    #     print(line)
    #     count += 1












    # rows = csv.reader(file, delimiter=';')    
    # rows.__next__()
    # for line in sorted(enumerate(filter(lambda i: int(i[1]) > int(i[2]), rows)), key=lambda x: x):
    #     print(line[1][0])
    # rows = csv.reader(file, delimiter=';')
    # for index, row in enumerate(filter(lambda i: int(i[1]) < int(i[2]), rows)):
    #     if index > 5:
    #         break
    #     print(row[0])
    







    # записываем первую строку с названиями столбцов
    # writer.writeheader()
    # # записываем строку с данными
    # writer.writerow({'first_col': 'value1', 'second_col': 'value2'})