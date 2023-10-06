def roundrobin(*args):
    b = [iter(i) for i in args]
    while b:
        try:
            for k, v in enumerate(b):
                try:
                    yield next(v)
                except StopIteration:
                    del b[k]
                    try:
                        yield next(b[k])
                    except IndexError:
                        continue
        except StopIteration:
            return 

# from itertools import cycle

# def take(iterable, n):
#     for elem, _ in zip(iterable, range(n)):
#         yield elem

# def roundrobin(*iterables):
#     non_empty = len(iterables)
#     iterables = cycle(map(iter, iterables))
#     while non_empty:
#         try:
#             for it in iterables:
#                 yield next(it)
#         except StopIteration:
#             non_empty -= 1
#             iterables = cycle(take(iterables, non_empty))