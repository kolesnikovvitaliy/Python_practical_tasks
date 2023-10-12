import re


a, b = map(int, input().split())
s = input()
regex_obj = re.compile(r'\d+')
result = sum(map(int, regex_obj.findall(s, pos=a, endpos=b)))
print(result)