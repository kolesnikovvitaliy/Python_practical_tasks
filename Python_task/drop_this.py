import itertools as it


def drop_this(iterable, obj):
    return it.dropwhile(lambda x: x == obj, iter(iterable))


numbers = [0, 0, 0, 1, 2, 3]

print(*drop_this(numbers, 0))