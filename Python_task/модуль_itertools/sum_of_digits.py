import itertools as it
import operator


def sum_of_digits(iterable):
    return max(it.accumulate(
        map(int, it.chain.from_iterable(
            map(str, iter(iterable)))), operator.add))


# def sum_of_digits(iterable):
#     return sum(map(int, it.chain.from_iterable(map(str, iterable))))

print(sum_of_digits([13, 20, 41, 2, 2, 5]))