from random import randint


def random_numbers(left, right):
    return iter(lambda: randint(left, right), left-1)