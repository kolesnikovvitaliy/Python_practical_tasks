def takes_positive(func):
    def wrapper(*args, **kwargs):
        str_in_args = {item for item in (*args, kwargs.values()) if
                       isinstance(item, (str, float))}
        neg_or_null_in_args = {item for item in (
            *args, *[items for items in kwargs.values()]) if item <= 0}
        if str_in_args:
            raise TypeError
        elif neg_or_null_in_args:
            raise ValueError
        else:
            return func(*args, **kwargs)
    return wrapper
