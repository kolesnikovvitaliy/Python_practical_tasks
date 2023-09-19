import functools


def returns_string(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        values = func(*args, **kwargs)
        if isinstance(values, str):
            return values
        raise TypeError
    return wrapper
