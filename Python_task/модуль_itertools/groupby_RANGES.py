import itertools as it


def ranges(numbers):
    key_sort = lambda x: numbers.index(x)-x
    groups = it.groupby(numbers, key=key_sort)
    lst = []
    for _, iter_result in groups:
        tmp = tuple(iter_result)
        x = tmp[0]
        y = tmp[-1]
        lst.append((x, y))

    return lst


numbers = [1, 2, 3, 4, 7, 8, 10]
# numbers = [1, 3, 5, 7]
# numbers = [1, 2, 3, 4, 5, 6, 7]
print(ranges(numbers))
# [(1, 4), (7, 8), (10, 10)]