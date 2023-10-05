import itertools as it


def take(iterable, n):
    return it.islice(iter(iterable), n)


print(*take(range(10), 5))