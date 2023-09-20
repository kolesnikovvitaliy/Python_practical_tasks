import functools


def add_attrs(**kwargs):
    def decorator(func):
        for k, v in kwargs.items():
            func.__setattr__(k, v)

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper
    return decorator
