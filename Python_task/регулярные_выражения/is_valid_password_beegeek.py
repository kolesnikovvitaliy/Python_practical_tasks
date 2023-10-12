import sys
from re import fullmatch

print(*(bool(fullmatch(r'^_\d+[a-zA-Z]*_?$', item)) for item in sys.stdin.read().splitlines()), sep="\n")