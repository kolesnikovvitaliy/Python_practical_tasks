import functools


def strip_range(start, end, char='.'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            values = func(*args, **kwargs)
            return values[:start] + char * len(values[start:end]) + values[end:]
        return wrapper
    return decorator
