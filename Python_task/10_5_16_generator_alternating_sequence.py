def alternating_sequence(count=None):
    i = 1
    while True:
        yield -i if i % 2 == 0 else i
        if count and i == count:
            return
        i += 1
