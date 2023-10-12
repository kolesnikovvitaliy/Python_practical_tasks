import sys
from re import fullmatch

for item in sys.stdin.read().splitlines():
    match1 = fullmatch(r'\b(\w+)\1\b', item)
    if match1:
        print(item)