def print_decorator(func):
    def print_wrapper(*args, **kwargs):
        args = (item.upper() if isinstance(item, str) else
                item for item in args)
        kwargs = {k: v.upper() if isinstance(v, str) else
                  {k: v} for k, v in kwargs.items()}
        func(*args, **kwargs)
    return print_wrapper


print = print_decorator(print)
