import itertools as it


def drop_while_negative(iterable):
    return it.dropwhile(lambda x: x < 0, iter(iterable))


iterator = iter([-3, -2, -1, 0, 1, 2, 3, -4, -5, -6])
# print(*drop_while_negative(iterator))
assert [0, 1, 2, 3, -4, -5, -6] == list(drop_while_negative(iterator))
