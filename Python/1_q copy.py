def build_query_string(params):
  a = set()
  for key, values in params.items():
    a.add(str(key) + '=' + str(params[key]))
  #sorted(a)
  b = "&".join(sorted(a))
  return b
print(build_query_string({'sport': 'hockey', 'game': 2, 'time': 17}))
print(build_query_string({'name': 'timur', 'age': 28}))

#for key in dict3:
    #result.setdefault(key, dict1[key]+dict3[key] if (key in dict2) and (key in dict1) else dict3[key])
# result = {}
# for i , *j in pets:
#     result.setdefault(tuple(j), []).append(i)