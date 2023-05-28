import time

def add(a, b, c):
    time.sleep(3)
    return a + b + c

def calculate_it(func, *args):
    start = time.perf_counter()
    a = func(*args)
    stop = time.perf_counter()
    print((a, stop-start))


calculate_it(add, 1, 2, 3)