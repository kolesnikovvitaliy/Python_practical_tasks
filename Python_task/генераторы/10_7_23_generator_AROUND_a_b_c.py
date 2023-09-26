def around(iterable):
    a = None
    if iterable:
        iterator = iter(iterable)
        first = next(iterator)
        yield from ((a, a := first, first := second)
                    for second in iterator)
        yield a, first, None


# def around(iterable):
#     it = iter(iterable)
#     a = None
#     b = next(it, None)
#     c = next(it, None)
#     while b != None:
#         yield a, b, c
#         a, b, c = b, c, next(it, None)