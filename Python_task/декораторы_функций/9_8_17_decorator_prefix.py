import functools


def prefix(string, to_the_end=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            values = func(*args, **kwargs)
            if to_the_end:
                values = values + string
            else:
                values = string + values
            return values
        return wrapper
    return decorator
