from itertools import cycle, count


def alnum_sequence():
    return cycle(x for i in map(lambda x, y: (x, chr(y)),
                                count(1), range(65, 91)) for x in i)


alnum = alnum_sequence()

print(*(next(alnum) for _ in range(55)))
