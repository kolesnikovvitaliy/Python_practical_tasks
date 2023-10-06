import itertools as it


def first_largest(iterable, number):
    try:
        return next(it.dropwhile(lambda x: x[1] < number, enumerate(iter(iterable))))[0]
    except StopIteration:
        return -1

# def first_largest(iterable, number):
#     return next(it.dropwhile(lambda x: x[1] < number, enumerate(iter(iterable))), (-1, ))[0]



iterator = iter([-1, -2, -3, -4, -5])

print(first_largest(iterator, 10))

iterator = iter([18, 21, 14, 72, 73, 18, 20])

print(first_largest(iterator, 10))