import re

result = re.split(r'\s*[,;.]\s*', input())

print(*result)