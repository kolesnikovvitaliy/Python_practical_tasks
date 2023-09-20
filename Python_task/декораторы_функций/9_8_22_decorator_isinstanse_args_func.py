import functools


def takes(*datatype):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = map(lambda x: isinstance(x, datatype),
                         [*args, *kwargs.values()])
            if all(result):
                values = func(*args, **kwargs)
                return values
            raise TypeError
        return wrapper
    return decorator
