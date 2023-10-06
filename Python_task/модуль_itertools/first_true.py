def first_true(iterable, predicate):
    return next(filter(predicate, iter(iterable)), None)


numbers = (0, 0, 0, 69, 1, 1, 1, 2, 4, 5, 6, 10, 100, 200)

print(first_true(numbers, None))