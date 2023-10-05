import itertools as it


def take_nth(iterable, n):
    return next(it.islice(iter(iterable), n-1, n), None)


numbers = [11, 22, 33, 44, 55]

print(take_nth(numbers, 3))