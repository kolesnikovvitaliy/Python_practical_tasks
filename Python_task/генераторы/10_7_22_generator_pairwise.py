def pairwise(iterable):
    if iterable:
        iterator = iter(iterable)
        first = next(iterator)
        yield from ((first, second, first := second)[:-1]
                    for second in iterator)
        yield first, None
