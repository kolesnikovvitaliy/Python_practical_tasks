from itertools import groupby, chain


text = input().split()

text.sort(key=lambda x: (len(x), x))
groups = groupby(text, key=lambda tmp: sum(1 for i in tmp))
for key, iter_text in groups:
    print(f'{key} ->', ', '.join(chain(iter_text)))

    
# hello beegeek stepik python