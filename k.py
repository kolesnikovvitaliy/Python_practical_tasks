import json 
import time
aaaa = time.monotonic()
a = dict()
with open("playgrounds.csv","r",encoding='utf8') as file_in, open("addresses.json","w",encoding='utf8') as file_onn:
   data = json.loads(file_in.read()) 
   
  
   json.dump(a, file_onn,indent=3)






bbbb = time.monotonic()
print(bbbb-aaaa)



# [a.setdefault(i['religion'], []).append(i['country']) for i in data]
#    json.dump(a, file_onn,indent=3)

# with open("people.json","r",encoding='utf8') as file_in, open("updated_people.json","w",encoding='utf8') as file_onn:
#     data = json.loads(file_in.read())
    
#     for i in range(len(data)):        
#         for j in set(y for k in data for y in k):
#             if j not in data[i]:
#                 data[i][j] = None      
#     json.dump(data, file_onn,indent=3)

# with open('people.json', encoding='utf8') as file, open('updated_people.json', 'w', encoding='utf8') as output:
#   data = json.load(file) 
#   keys={k:None for row in data for k in row.keys()}
#   result=[{**keys, **row} for row in data]
#   json.dump(result, output, indent=3)  
# with open('people.json', 'r', encoding='utf-8') as r, open('updated_people.json', 'w', encoding='utf-8') as w:
#     data = json.load(r)
#     all_keys = set(key for i in data for key in i.keys())
# #     json.dump([i | dict.fromkeys(all_keys - i.keys(), None) for i in data], w)
# with open('people.json', encoding='utf8') as fi, open('updated_people.json', 'w') as fo:
#     people = json.load(fi)
#     d = {k: None for i in people for k in i.keys()}
#     json.dump([d | i for i in people], fo)


# with open('data.json', 'r', encoding = 'UTF-8') as file:
#   obj = json.load(file)
#   types = {
#     str: lambda x: x + '!',
#     int: lambda x: x + 1,
#     bool: lambda x: not x,
#     list: lambda x: x * 2,
#     dict: lambda x: (x.update({"newkey": None}), x)[1]
#   }
#   out = list(map(lambda x: types[type(x)](x), filter(lambda x: x != None, obj)))
# with open('updated_data.json', 'w', encoding = 'UTF-8') as file:
#   json.dump(out, file)
# import json as js

# with open('data.json', encoding='utf-8') as file, open('updated_data.json', 'w', encoding='utf-8') as out:
#     d = {str: lambda x: x + '!', int: lambda x: x + 1, bool: lambda x: bool(abs(x - 1)),
#          list: lambda x: x * 2, dict: lambda x: x | {'newkey': None}}
#     js.dump([(x := (d[type(i)])(i)) for i in js.load(file) if not i is None], out)    
#     print(json.dumps(a, indent=3))
    
    #print(list(filter(lambda x: x!="",a)))

    #print(data)
#file_in = ["Hello", 179, true,null, [1, 2, 3], {"key": "value"}]
# for i in filter(null,file_in):
#     print(type(i))
#     print(i)
#     a = [str, int, bool, list, dict].index(type(i))
#     c = [["i+'!'"],['i+1'],['not bool(i)'],['i*2'],['i | {"newkey":  null}']][a]
#     b.append(eval(*c)) 
#     print(b)

    # a = [eval(*[["i+'!'"],['i+1'],['i'],['i*2'],['i | {"newkey": null}']][[str, int, bool, list, dict].index(type(i))]) for i in filter(null,data)]
    # file_onn.write(json.dumps(a))
######################################################################################
#print(data)
#file_in = ["Hello", 179, true,null, [1, 2, 3], {"key": "value"}]
# for i in filter(null,file_in):
#     print(type(i))
#     print(i)
#     a = [str, int, bool, list, dict].index(type(i))
#     c = [["i+'!'"],['i+1'],['not bool(i)'],['i*2'],['i | {"newkey":  null}']][a]
#     b.append(eval(*c)) 
#     print(b)
#######################################################################################
# если объект является строкой, в его конец добавляется восклицательный знак
# если объект является числом, он увеличивается на единицу
# если объект является логическое значением, он инвертируется
# если объект является списком, он удваивается
# если объект является JSON-объектом (словарем), в него добавляется новая пара "newkey": null
# если объект является пустым значением (null), он не добавляется
# Полученный список программа должна записать в файл updated_data.json.

# Примечание 1. Например, если бы файл data.json имел вид:

# ["Hello", 179, true, null, [1, 2, 3], {"key": "value"}]
# то программа должна была бы создать файл updated_data.json со следующим содержанием:

# ["Hello!", 180, false, [1, 2, 3, 1, 2, 3], {"key": "value", "newkey": null}]

# # sys.stdin.rea()  # это строка -> применяем json.loads
# data = json.loads(sys.stdin.read())             
# for key, value in data.items():
#     if type(value) == list:
#         print(f'{key}: {", ".join(map(str, value))}')
#     else:d
#         print(f'{key}: {value}')


#{"size": 36, "style": "bold", "name": "text1", "alignment": "center"}

# import json

# with open('data.json') as file:
#     data = json.load(file)                # передаем файловый объект
#     for key, value in data.items():
#         if type(value) == list:
#             print(f'{key}: {", ".join(value)}')
#         else:
#             print(f'{key}: {value}')


# def is_correct_json(data):
#     try:
#         json.loads(data)
#         return True
#     except:
#         return False
# data = '{"name": "Barsik", "age": 7, "meal": "Wiskas"}'

# print(is_correct_json(data))


# club1 = {"name": "FC Byern Munchen", "country": "Germany", "founded": 1900,
#          "trainer": "Julian Nagelsmann", "goalkeeper": "M. Neuer", "league_position": 1}

# club2 = {"name": "FC Barcelona", "country": "Spain", "founded": 1899,
#          "trainer": "Xavier Creus", "goalkeeper": "M. Ter Stegen", "league_position": 7}

# club3 = {"name": "FC Manchester United", "country": "England", "founded": 1878,
#          "trainer": "Michael Carrick", "goalkeeper": "D. De Gea", "league_position": 8}

# with open('data.json', 'w', encoding='utf8') as file:
#     file.write(json.dumps([club1,club2,club3], indent=3))         
# import json

# specs = {
#          'Модель': 'AMD Ryzen 5 5600G',
#          'Год релиза': 2021,
#          'Сокет': 'AM4',
#          'Техпроцесс': '7 нм',
#          'Ядро': 'Cezanne',
#          'Объем кэша L2': '3 МБ',
#          'Объем кэша L3': '16 МБ',
#          'Базовая частота': '3900 МГц'
#         }

# specs_json = json.dumps(specs, ensure_ascii=False,indent=3)

# print(specs_json)