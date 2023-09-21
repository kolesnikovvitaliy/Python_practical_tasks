def starmap(func, iterable):
    # return (func(*i) for i in iterable)
    return map(lambda x: func(*x), iterable)
