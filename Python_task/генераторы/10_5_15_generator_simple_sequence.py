def simple_sequence():
    i = 1
    while True:
        for _ in range(i):
            yield i
        i += 1
