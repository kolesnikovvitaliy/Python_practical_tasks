import itertools as it

text = input()
# 'aab'
[print(''.join(i)) for i in sorted(set(it.permutations(text, r=len(text))))]
