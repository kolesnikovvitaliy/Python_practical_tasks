import sys
from array import array

n, parents = int(input()), map(int, sys.stdin.read().split())
_lst = [array('i') for i in range(n + 1)]
[_lst[next(parents)].append(i) for i in range(n)]

root, count = _lst[-1], 0
while root:
    queue, root = root, []
    for index in queue:
        root += _lst[index]
        print(_lst)
    count += 1
print(count)

# 10
#9 7 5 5 2 9 9 9 2 -1
#res = 4