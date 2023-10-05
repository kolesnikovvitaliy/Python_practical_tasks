import itertools as it


def ncycles(iterable, times):
    return it.chain(*it.tee(iter(iterable), times))


print(*ncycles([1, 2, 3, 4], 3))