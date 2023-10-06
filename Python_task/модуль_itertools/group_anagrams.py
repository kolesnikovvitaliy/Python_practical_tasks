from itertools import groupby


def group_anagrams(words):
    words = sorted(words, key=sorted)
    groups = groupby(words, key=sorted)
    for _, iter_result in groups:
        yield tuple(iter_result)


groups = group_anagrams(['крона', 'сеточка', 'тесачок', 'лучик', 'стоечка', 'норка', 'чулки'])

print(*groups)