import csv
import time
aaaa = time.monotonic()

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

bbbb = time.monotonic()
print(bbbb-aaaa)