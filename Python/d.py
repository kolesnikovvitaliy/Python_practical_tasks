import sys
from datetime import datetime

a = [int(i.strip('\n')) for i in sys.stdin]


if len(a) == len(set(a)):
    if len(a) == a[-1]:
        print('Арифметическая прогрессия')
    elif a[-1]/2 == a[-2]:
        print('Геометрическая прогрессия')
    else:
        print('Не прогрессия')

else:
    print('Не прогрессия')

# a = sys.stdin
# lst= {}
# for i in a:
#     if len(i) > 20:
#         b, c, d = i.split('/')
#         lst.setdefault(c.strip(), []).append([b.strip(), d.strip(' \n')])
#     else:
#         for j in sorted(lst[i.strip()], key=lambda x: (x[1], x)):
#             print(j[0],sep="\n")

# *lst, f = [[j.strip() for j in i.split('/')] for i in open(0)]
# print(lst)
# [print(i[0]) for i in sorted(lst, key=lambda x: (float(x[2]), x[0])) if i[1] in f]



















# import sys
# a = sys.stdin
# b = ''
# for i in a:
#     if i.strip(' ').startswith('#'):
#         continue
#     else:
#         b += i
#print(b)








# if len(a) > 0:
#     print('Рост самого низкого ученика:', min(a))
#     print('Рост самого высокого ученика:', max(a))
#     print('Средний рост:', round(sum(a)/len(a), 1))
# else:
#     print('нет учеников')


# a = [int(i) for i in sys.stdin]

# for i in range(len(a)):
#     if i % 2 == 0:
#         b = 'Анри'
#     else:
#         b = 'Дима'
#     if a[i] % 2 != 0:
#         if b == 'Анри':
#             b = 'Дима'
#         elif b == 'Дима':
#             b = 'Анри'
# print(b)
# print(a)
# import sys
# numbers = [int(line.strip("\n")) for line in sys.stdin]
# print("Анри" if (len(numbers) + numbers[-1]) % 2 else "Дима")








# from datetime import datetime
# line = list(map(str, sys.stdin))
# a = []

# for i in range(len(line)):
#      #print(line[i].strip('\n'))
#      a.append(datetime.strptime(line[i].strip('\n'), '%Y-%m-%d'))

# print((max(a)-min(a)).days)

# import sys
# from datetime import datetime
# date = [datetime.fromisoformat(i.strip()) for i in sys.stdin]
                              
# print((max(date) - min(date)).days)