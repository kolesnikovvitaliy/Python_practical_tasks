from collections import defaultdict


def wins(pairs):
    result_dict = defaultdict(set)
    [result_dict[i[0]].add(i[1]) for i in pairs]
    return result_dict



result = wins([('Артур', 'Дима'), ('Артур', 'Тимур'), ('Артур', 'Анри'), ('Дима', 'Артур')])

for winner, losers in sorted(result.items()):
    print(winner, '->', *sorted(losers))