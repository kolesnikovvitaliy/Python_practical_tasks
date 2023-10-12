# import sys
# from re import search, IGNORECASE

# beegeek = 0
# for item in sys.stdin.read().splitlines():
#     if search(r'beegeek', item, IGNORECASE):
#         beegeek += 1

# print(beegeek)

import sys, re

print(sum(bool(re.search(r'beegeek', s, re.I)) for s in sys.stdin))
