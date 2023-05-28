import json 
import csv
import datetime
import time
aaaa = time.monotonic()
d = dict()
b = []
with open("food_services.json","r",encoding='utf8') as file_in:
    data = json.loads(file_in.read())
    [d.setdefault(i['TypeObject'],[]).append([i['Name'], i['SeatsCount']]) for i in data]
    # print([d[i][0] for i in sorted(d,key=lambda x: (sorted(d[x],key=lambda y: int(y[1]),reverse=True)))])
    [b.append([key,*sorted(voluem,key=lambda x: int(x[1]),reverse=True)[0]]) for key, voluem in sorted(d.items())]
    for i in b:
        print(f'{i[0]}: {i[1]}, {i[2]}')
#  [a.setdefault(i[4],[]).append([*i[0:3],datetime.datetime.strptime(i[3],'%Y-%m-%d %H:%M:%S') ]) for i in rows[1:]]
#     [b.append([*sorted(voluem,key=lambda x: (int(x[2]), x[3]),reverse=True)[0],key]) for key, voluem in sorted(a.items())]
#     c = [dict(zip(['name', 'surname', 'best_score', 'date_and_time', 'email'], [i[0],i[1],int(i[2]),datetime.datetime.strftime(i[3],'%Y-%m-%d %H:%M:%S'),i[4]])) for i in b]
#     file_onn.write(json.dumps(c, indent=3))


bbbb = time.monotonic()
print(bbbb-aaaa)






# def get_sum_mag(data, lst):

#     for j in lst:
#         d = dict()    
#         [d.setdefault(i[j],[]).append([]) for i in data]
#         a = sorted(d,key=lambda x: len(d[x]))[-1]
#         if len(a) > 0:
#             print(f'{a}: {len(d[a])}')
#         else:
#             b = sorted(d,key=lambda x: len(d[x]))[-2]
#             print(f'{b}: {len(d[b])}')
    
# with open("food_services.json","r",encoding='utf8') as file_in:
#     data = json.loads(file_in.read())
#     lst = ['District','OperatingCompany']
#     get_sum_mag(data, lst)



#     # [d.setdefault(i['District'],[]).append([]) for i in data]
#     [d.setdefault(i['District'],[]).append([])  for i in data]
#     [o.setdefault(i['OperatingCompany'],[]).append([])  for i in data]
#     a = sorted(d,key=lambda x: len(d[x]))[-1]
#     b = sorted(o,key=lambda x: len(o[x]))[-2]
#     print(f'{a}: {len(d[a])}')
#     print(f'{b}: {len(o[b])}')

# d = dict()
# o = dict()
# with open("food_services.json","r",encoding='utf8') as file_in:
#     data = json.loads(file_in.read())
#     # [d.setdefault(i['District'],[]).append([]) for i in data]
#     [d.setdefault(i['District'],[]).append([])  for i in data]
#     [o.setdefault(i['OperatingCompany'],[]).append([])  for i in data]
#     a = sorted(d,key=lambda x: len(d[x]))[-1]
#     b = sorted(o,key=lambda x: len(o[x]))[-2]
#     print(f'{a}: {len(d[a])}')
#     print(f'{b}: {len(o[b])}')
    # print(len(d['Тверской район']))
    #[i['Name'],i['OperatingCompany'],i['Address']]
    # print(d)
    # a[i[1]] = a.get(i[1], 0) + int(i[-1])






# a = dict()
# b = []

# with open("exam_results.csv","r",encoding='utf8') as file_in, open("best_scores.json","w",encoding='utf8') as file_onn:
#     rows = list(csv.reader(file_in, delimiter=","))
#     # print(rows[0])
#     [a.setdefault(i[4],[]).append([*i[0:3],datetime.datetime.strptime(i[3],'%Y-%m-%d %H:%M:%S') ]) for i in rows[1:]]
#     [b.append([*sorted(voluem,key=lambda x: (int(x[2]), x[3]),reverse=True)[0],key]) for key, voluem in sorted(a.items())]
#     c = [dict(zip(['name', 'surname', 'best_score', 'date_and_time', 'email'], [i[0],i[1],int(i[2]),datetime.datetime.strftime(i[3],'%Y-%m-%d %H:%M:%S'),i[4]])) for i in b]
#     file_onn.write(json.dumps(c, indent=3))
# result = {}
# with open('exam_results.csv', encoding='utf-8') as ex_r:
#     rows = csv.DictReader(ex_r)  # 1
#     for row in rows:
#         row['best_score'] = int(row.pop('score'))  # 2
#         r = result.get(row['email'], row)  # 3
#         best_row = max(r, row, key=lambda item: (item['best_score'], item['date_and_time']))  # 4
#         result[row['email']] = best_row  # 5 

# with open('best_scores.json', 'w', encoding='utf-8') as bs:
#     out = sorted(result.values(), key=lambda item: item['email'])  # 6
#     json.dump(out, bs, indent=3)  # 7    
    
   
    # [b.append([*list(filter(lambda x: (int(x[2]), x[3]),voluem)),key]) for key, voluem in sorted(a.items())]  
        #sorted(a,key=lambda x: (sorted(a[x],key=lambda y: int(y[2]),reverse=True)))
    #b = sorted(a,key=lambda x: (x,sorted(a[x],key=lambda y: int(y[2]),reverse=True)))
    
    #print([a[i] for i in sorted(sorted(a, key=lambda y: (sorted(a[y],key=lambda k: int(k[2]),reverse=True))),key=lambda x: x)])
    #print(b['aardo@mac.com'])
    # for key, voluem in a.items():
    #     #print(sorted(voluem,key=lambda x: (int(x[2]), x[3]),reverse=True))
    #     b.append([sorted(voluem,key=lambda x: (int(x[2]), x[3]),reverse=True)[0],key])
   
        #break





# bbbb = time.monotonic()
# print(bbbb-aaaa)
# a = []
# with open("pools.json","r",encoding='utf8') as file:
#     data = json.loads(file.read())
#     for i in sorted(data,key=lambda x: (int(x['DimensionsSummer']['Length']),int(x['DimensionsSummer']['Width'])),reverse=True):   
#         if time.strptime(i['WorkingHoursSummer']['Понедельник'][0:4], "%H:%M") <= time.strptime('10',"%H") and time.strptime(i['WorkingHoursSummer']['Понедельник'][6:-1], "%H:%M") >= time.strptime('12',"%H"):
#             print(i['DimensionsSummer']['Length'],i['DimensionsSummer']['Width'],sep="x")
#             print(i['Address'])
#             break    
        
    # print(a)
# with open("students.json","r",encoding='utf8') as file_in, open("data.csv","w",encoding='utf8') as file_onn:
#     data = json.loads(file_in.read())
#     a = sorted(map(lambda x: [x['name'],x['phone']], filter(lambda j: (j['age'] >= 18 and int(j['progress']) >= 75),data)),key=lambda y: y[0])

#     writer = csv.writer(file_onn)
#     writer.writerow(['name', 'phone'])
#     writer.writerows(a)
# with open('students.json', encoding='utf8') as fi, \
#         open('data.csv', 'w', newline='') as fo:
# 	students, w = json.load(fi), csv.writer(fo)
# 	w.writerow(['name' ,'phone'])
# 	w.writerows(sorted([[i['name'], i['phone']] for i in students \
#                         if i['age'] >= 18 and i['progress'] >= 75]))
# with open('students.json') as file:
#     students = json.load(file)
#     result = []
#     for student in students:
#         if student['age'] >= 18 and student['progress'] >= 75:
#             result.append([student['name'], student['phone']])
#     result.sort()
        
# with open('data.csv', 'w', encoding='utf-8', newline='') as file:
#     writer = csv.writer(file)
#     writer.writerow(['name', 'phone'])
#     writer.writerows(result)    
    # for i in range(len(data)):        
    #     for j in set(y for k in data for y in k):
    #         if j not in data[i]:
    #             data[i][j] = None  
    # for i in rows[1:]:
    #     a.setdefault(i[1],{}).setdefault(i[2],[]).append(i[3])
    # [a.setdefault(i[1],{}).setdefault(i[2],[]).append(i[3]) for i in rows[1:]]
    # json.dump(a, file_onn,indent=3,ensure_ascii=False)



    # writer = csv.writer(file_onn)
    # writer.writerow(['name', 'phone'])
    # writer.writerows(a)




# with open("playgrounds.csv","r",encoding='utf8') as file_in, open("addresses.json","w",encoding='utf8') as file_onn:
#     rows = list(csv.reader(file_in, delimiter=";"))
#     for i in rows[1:]:
#         a.setdefault(i[1],{}).setdefault(i[2],[]).append(i[3])
#     # [a.setdefault(i[1],{}).setdefault(i[2],[]).append(i[3]) for i in rows[1:]]
#     json.dump(a, file_onn,indent=3,ensure_ascii=False)

# for i in range(len(data)):        
#         for j in set(y for k in data for y in k):
#             if j not in data[i]:
#                 data[i][j] = None      
#     json.dump(data, file_onn,indent=3)
# a = dict()
# with open('wifi.csv', 'r' ,encoding="utf-8") as file:
#     rows = list(csv.reader(file, delimiter=";"))
#     for i in rows[1:]:
#         a[i[1]] = a.get(i[1], 0) + int(i[-1])
#     result = sorted(sorted([[i, a[i]] for i in a], key=lambda x: x[0]), key=lambda y: int(y[1]), reverse=True)
    
   