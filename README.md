## В этом репозитории расположенны, некоторые, решенные мной задачи на Python

#### Несколько примеров
* Работа с датой и временем 
```python
from datetime import datetime

def get_in_list(data):
    d = []    
    if type(data) == str:
        d.append(data)
        return d
    return data       

def get_list_dates(data):
    from datetime import timedelta as t
    a = []
    b = []
    for i in get_in_list(data):
        if len(i) < 15:
            a.append(datetime.strptime(i,'%d.%m.%Y'))
        else:
            b.append([datetime.strptime(y,'%d.%m.%Y') for y in [j for j in i.split('-')]])
    for i in range(len(b)):
        a.append(b[i][0])
        while b[i][1] not in a:
            b[i][0] += t(days=1)
            a.append(b[i][0])
    return a    
         
def is_available_date(dates, some_date):
    for i in get_list_dates(some_date):
        if i in get_list_dates(dates):
            return False
    return True

dates = ['04.11.2021', '05.11.2021-09.11.2021']
some_date = '06.11.2021'
print(is_available_date(dates, some_date))



# dates = ['04.11.2021', '05.11.2021-09.11.2021']
# some_date = '01.11.2021-04.11.2021'
# print(is_available_date(dates, some_date))
 ``` 
*   Работа с данными
```python
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv('final_data.csv')
#print(data.head(5))
#print(data.columns)
data = data[['bathrooms', 'bedrooms', 'finishedsqft', 'lastsoldprice', 'zestimate']]
#print(data[['bathrooms', 'bedrooms']].cov())
#print(data[['bathrooms', 'bedrooms']].corr('spearman'))
#print(data[['bathrooms', 'bedrooms']].describe())
#print(data[['bathrooms', 'bedrooms']].var())
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr('spearman'))
plt.show()
#print(data.corr())
 ``` 
  
```python
from numpy import random as rnd
from matplotlib import pyplot as plt
import scipy.stats as stats
import numpy as np

data = rnd.normal(0, 1, 10000)
index = np.arange(data.shape[0])
stats.probplot(data, dist="norm", plot=plt)
plt.show()
plt.plot(index, data)
plt.show()
plt.hist(data)
plt.show()
uniform_data = rnd.uniform(size=1000)
stats.probplot(uniform_data, dist="norm", plot=plt)
plt.show()
 ``` 
 * Простая выборка данных методами Python, несколько способов решения одной задачи
```python
import csv
import time


with open('prices.csv', 'r' ,encoding="utf-8") as file_in:
    rows = list(csv.reader(file_in, delimiter=";"))    
    b = rows[0][1:]
    f, s, n = sorted([[b[j[1][1:].index(str(min(map(int,j[1][1:]))))+1],j[0],min(map(int,j[1][1:])) ] for j in [[i[0],i[1:]] for i in rows[1:]]], key=lambda x: (int(x[2]),x[0],x[1]))[0]
    
print(f'{f}: {s}')

######################################################################################################3
# a = dict()
# e = dict()
# with open('prices.csv', 'r' ,encoding="utf-8") as file_in:
#     rows = list(csv.reader(file_in, delimiter=";"))        
#     [a.setdefault(rows[0][y],[]).append(rows[1:][i][y]) for i in range(len(rows[1:])) for y in range(len(rows[1:][i]))]
#     b = rows[0][0]
# for i in sorted(a, key=lambda x: len(x)):
#     if i == b:
#         continue
#     [e.setdefault(i,[]).append([a[b][a[i].index(str(min(map(int,a[i]))))], min(map(int,a[i]))])]
    
# c = sorted(e,key=lambda x: (e[x][0][1],x))[0]
# print(f'{c}: {e[c][0][0]}')
##########################################################################################
# with open('prices.csv', encoding='utf-8') as f:
#     shop_names, *goods = zip(*csv.reader(f, delimiter=';'))
#     shops = list(shop_names[1:])
#     prices = {food: list(zip(map(int, price), shops)) for food, *price in goods}

# cheapest = min([(min(v)[0], k, min(v)[1]) for k,v in prices.items()])
# print(f'{cheapest[1]}: {cheapest[2]}')
#############################################################################################
# with open('prices.csv', encoding='UTF-8') as f:
#     h, *rows = csv.reader(f, delimiter=';')
# goods = [(r[0], h[x], r[x]) for r in rows for x in range(1, len(h))]
# cheapest = min(goods, key=lambda x: (int(x[2]), x[1], x[0]))
# print(cheapest)

# print(f'{cheapest[1]}: {cheapest[0]}')
###############################################################################################3

# with open('prices.csv', encoding='utf-8') as file:
#     reader = list(csv.reader(file, delimiter = ';'))
#     data = []
#     for i in range(1, len(reader)):
#         for j in range(1, len(reader[0])):
#             data.append([int(reader[i][j]),reader[0][j], reader[i][0]])
#     ans = min(data)
#     print(f'{ans[1]}: {ans[2]}')

 ``` 
 * Возведение Квадратной матрици в квадрат
```python
#  Формат ввода матрицы
# 5- матрица квадратная
# 1 2 1 1 2
# 3 3 3 3 3
# 1 2 1 1 2
# 3 3 3 3 3
# 1 2 1 1 2
# 3 - степень
n = int(input())
matrix = [[int(i) for i in input().split()] for _ in range(n)]
matrix_2 = [[0] * n for i in range(n)]
f = int(input())
for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_2[i][j] += matrix[i][k] * matrix[k][j]
                
def res(n, matrix, matrix_2):
    matrix_3 = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            for k in range(n):
                matrix_3[i][j] += matrix[i][k] * matrix_2[k][j]
    matrix_2 = matrix_3
    return matrix_3, matrix_2 

if f > 2:
    for _ in range(f-2):
        matrix_3, matrix_2 = res(n, matrix, matrix_2)
    for i in matrix_3:
        print(*i)     
else:
    for i in matrix_2:
        print(*i)
 ``` 
 #### И много других задач. В этом репозитории к сожалению, грубо говоря, не все.
 