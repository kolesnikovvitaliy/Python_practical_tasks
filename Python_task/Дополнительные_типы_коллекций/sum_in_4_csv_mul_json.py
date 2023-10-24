from collections import Counter
import csv
import json

res = Counter()
for i in range(4):
    with open(f'quarter{i + 1}.csv', encoding='utf-8') as file:
        text = csv.reader(file, delimiter=',')
        head = next(text)
        sum_values = map(lambda x: (x[0], sum(map(int, x[1:]))),
                         map(lambda x: x, text))
        res += Counter({k: v for k, v in sum_values})

with open('prices.json', encoding='utf=8') as f:
    text = json.loads(f.read())
    for i in res:
        res[i] *= text[i]

print(res.total())