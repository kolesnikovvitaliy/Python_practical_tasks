# def outer_func(a, b):
#     def inner_func(c, d):
#         return c + d + a*b
#     return inner_func

# res = outer_func(5, 10)(3, 2)

# print(res)
# def generate_letter(mail, name, date, time, place, teacher='Тимур Гуев', number=17):
#     return f'''To: {mail}
# Приветствую, {name}!
# Вам назначен экзамен, который пройдет {date}, в {time}.
# По адресу: {place}. 
# Экзамен будет проводить {teacher} в кабинете {number}. 
# Желаем удачи на экзамене!'''
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))
#print((lambda x: (x + 3) * 5 / 2)(3))
# data = [['p', 'y', 't', 'h', 'o', 'n'], ['s', 't', 'e', 'p', 'i', 'k']]
# result = list(map(lambda x: '.'.join(x), data))
# print(result[1])

# result = list(filter(str.swapcase, ['a', '1', '', 'b', '2']))

# print(result)
# files = ['duwwouy440.py', 'crocst0sse.cs', 'j9t7ga2s6x.java', 'jk4nnes4tp.py', '2spc9uqzhu.doc', 
#          'qi0ujxe0c7.png', 'z5x7l1j1d8.jpg', 'i5wtdxh366.geo', 'h53s2m2p73.py', 'ojty11f02d.sx', 
#          'jyjuwlvwb3.st', 'gv4940lf8m.txt', 'op38fy9m9x.docx', 'o02ltr8vbp.xlsx', 'la97gc4js4.html', 
#          'lcihrp8c6l.py', 'z66y7dgfo1.py', 'ckoks0849e.csv']

# result = list(filter(lambda s: s.endswith('.py'), files))

# print(len(result))
#print(list(filter(None, ['', 1, 7, 'beegeek', None, False, 0])))
# from functools import reduce

# numbers = [1, 2, 3]
# result = reduce(lambda x, y: x + y, numbers)
# print(result)
# from functools import reduce

# numbers = [1, 2, 3]
# result = reduce(lambda a, b: a * b, numbers, 10)
# print(result)
# from functools import reduce

# words = ['beegeek', 'stepik', 'python', 'iq-option']
# result = reduce(lambda a, b: a if len(a) > len(b) else b, words)
# print(result)!=x[::-1]
# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# #print(*map(lambda x: , numbers))
# print(*list(filter(lambda x: str(x) != str(x)[::-1], numbers)))
# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
# sorted_numbers = sorted(numbers, key=lambda x:sum(x)/len(x),reverse=True)
# # print(sorted_numbers)
#print(*sorted([input() for _ in range(int(input()))], key=lambda x: [*map(int, x.split('.'))]), sep='\n')
# def gemValue(word):
#     return sum(map(lambda l: ord(l.upper()) - ord('A'), word)), word
# words = [input() for _ in range(int(input()))]
# print(*sorted(words, key=gemValue), sep='\n')
#with open('ledger.txt', encoding='utf-8') as in_file:
# counter = 0
# a = ['$1','$2']
# for i in a:
#     counter += int(i.rstrip()[1:])
# print("$", counter, sep="")
# arr = []
# a = 0
# with open('grades.txt') as file:
#     for line in file.readlines():
#         if (int(line.strip().split()[1]) >= 65) and (int(line.strip().split()[2]) >= 65) and (int(line.strip().split()[3]) >= 65):
#             a += 1

# print(a)
# my_str = []
# my_list = []
# my_count = []
# with open('students.csv') as file:
#     for line in file.read().split():
#         a = line.split(",")
#         my_str.append(a)
# for i in range(2,len(my_str)):
#     my_list.append(my_str[i][1].title())
# my_count = max(my_list,key=my_list.count)
# print(my_count)    
# for i in my_list:
#     b = my_list.count(i) 
#     my_count.append(b)
# max_count = max(my_count)
# for i in my_list:
#     if my_list.count(i) == max_count:
#         result.append(i)
# print(*result, sep=",")
# my_count = max(my_list,key=my_list.count)
# print(my_count)
# #     for line in file.read().split():
#         if max_len <= len(line):
#             max_len = len(line)  

# with open('students.csv') as file:       
         
#     for line in file.read().split():
#         if max_len == len(line):
#             max_str.append(line)   

# for elem in max_str:
#     print(elem, end = '\n')
# import csv
# import statistics

# with open("students.csv", encoding="utf-8") as file:
#     names = [user[1].title() for user in list(csv.reader(file))[1:]]

# print(*statistics.multimode(names), sep=", ")
from itertools import islice
import statistics as st 
with open("data.csv", "r", encoding = "utf-8") as fin:
    sall_list = [int(line.split(',')[4]) for line in islice(fin, 1, None)]
        
print('Средняя заработная плата =', int(st.mean(sall_list)))
print('Медианная заработная плата =', int(st.median(sall_list)))
print('Размах выборки =', max(sall_list) - min(sall_list))































