import time


def timer(func):
    res = 0
    
    def wrapper(*args, **kwargs):
        nonlocal res
        start = time.perf_counter()
        val = func(*args, **kwargs)
        work_time = time.perf_counter() - start
        res += work_time
        # print(f'Время выполнения {func.__name__}: {work_time} сек.')
        print(f'Время выполнения {func.__name__}: {res} сек.')
        return val
    return wrapper

