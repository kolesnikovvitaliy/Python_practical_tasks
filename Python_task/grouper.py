import itertools as it


def grouper(iterable, n):
    return it.zip_longest(*it.repeat(iter(iterable), n))


iterator = iter([1, 2, 3, 4, 5, 6, 7])

print(*grouper(iterator, 3))