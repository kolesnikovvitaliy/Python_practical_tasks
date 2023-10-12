import sys 
from re import fullmatch
import itertools as it

name_key = it.cycle(('Код страны', 'Код города', 'Номер'))
for item in sys.stdin.read().splitlines():
    match1 = fullmatch(r"(?P<country>\d+)[- ](?P<citi>\d+)[- ](?P<num>\d+)", item)
    [print(', '.join(f'{next(name_key)}: {v}' for v in match1.groupdict().values()))]


# from re import search

# regex = r'(\d{1,3})([- ])(\d{1,3})\2(\d{4,10})'

# for n in open(0):
#     code = search(regex, n)
#     print(f'Код страны: {code[1]}, Код города: {code[3]}, Номер: {code[4]}')