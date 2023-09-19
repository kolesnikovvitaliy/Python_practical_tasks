import functools


def ignore_exception(*args):
    ignore_exception = args

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                values = func(*args, **kwargs)
                return values
            except Exception as e:
                if type(e) in ignore_exception:
                    print(f'Исключение {type(e).__name__} обработано')
                else:
                    raise type(e)
        return wrapper
    return decorator
