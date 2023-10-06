import itertools as it


lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

n = int(input())
m = int(input())

print(*(''.join(i) for i in it.product(it.takewhile(lambda item: item <= lst[n-1], lst), repeat=m)))

#2
#3

#3
#2

#16
#2