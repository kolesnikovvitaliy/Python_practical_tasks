import functools


def trace(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f'TRACE: вызов {func.__name__}() с аргументами: {args}, {kwargs}')
        values = func(*args, **kwargs)
        print(f'TRACE: возвращаемое значение {func.__name__}(): {repr(values)}')
        return values
    return wrapper
