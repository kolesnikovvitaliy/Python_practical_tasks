import re
import sys

regex = r'[Кк]од'
string = enumerate(sys.stdin.read().splitlines(), 1)
for items in string:
    if (result := re.search(regex, items[1])):
        print(f'{items[0]} {result.start()}')
        # выводит номер строки и индекс начала слова код
        break
else:
    print('код не найден')