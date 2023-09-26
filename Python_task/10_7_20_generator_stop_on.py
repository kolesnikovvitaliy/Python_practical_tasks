def stop_on(iterable, obj):
    for i in iterable:
        if i == obj:
            return
        yield i
    
# def stop_on(iterable, obj):
#     it = iter(iterable)
#     return iter(lambda: next(it), obj)
