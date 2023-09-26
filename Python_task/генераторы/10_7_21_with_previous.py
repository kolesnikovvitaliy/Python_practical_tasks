def with_previous(iterable):
    a = None
    for i in iterable:
        yield (i, a)
        a = i