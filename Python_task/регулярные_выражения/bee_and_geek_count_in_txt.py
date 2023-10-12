import sys
from re import search

bee = geek = 0
for item in sys.stdin.read().splitlines():
    if search(r'(.*bee.*){2,}', item):
        bee += 1
    if search(r'(\bgeek\b)+', item):
        geek += 1

print(bee, geek, sep="\n")
