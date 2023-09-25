def interleave(*args):
    for item in zip(*args):
        yield from item
