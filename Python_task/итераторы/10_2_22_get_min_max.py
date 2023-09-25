def get_min_max(data):
    import copy
    is_trye_range = copy.deepcopy(data)
    if not hasattr(data, '__next__') and data:
        return min(data), max(data)
    elif hasattr(data, '__next__') and next(is_trye_range, 'stop') != 'stop':
        min_range = copy.deepcopy(data)
        max_range = copy.deepcopy(data)
        return min(min_range), max(max_range)
    else:
        return

# def get_min_max(iterable):
#     iterable = iter(iterable)
#     try:
#         smallest = largest = next(iterable)
#     except Exception:
#         return None
#     for elem in iterable:
#         if elem < smallest:
#             smallest = elem
#         if elem > largest:
#             largest = elem
#     return smallest, largest
