import itertools as it


def max_pair(iterable):
    return max(map(sum, it.pairwise(iter(iterable))))


iterator = iter([0, 0, 0, 0, 0, 0, 0, 0, 0])

print(max_pair(iterator))