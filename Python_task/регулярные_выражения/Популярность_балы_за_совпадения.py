import sys 
import re
a = 0
for item in sys.stdin.read().splitlines():
    if re.fullmatch(r'^(beegeek).*(beegeek)$', item):
        a += 3
    elif re.search(r'.*(beegeek)$', item):
        a += 2
    elif re.match(r'^(beegeek).*', item):
        a += 2
    elif re.fullmatch(r'.*(beegeek).*', item): 
        a += 1
print(a)


# total = 0
# ssd = {r'^beegeek.*beegeek$': 3, 
#        r'^beegeek|.*beegeek$': 2,
#        r'beegeek': 1}
# for i in sys.stdin:
#     for j in ssd.keys():
#         if re.search(j, i.rstrip()): 
#             total += ssd[j]
#             break
# print(total)