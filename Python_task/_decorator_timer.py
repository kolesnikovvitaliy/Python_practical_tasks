import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        val = func(*args, **kwargs)
        work_time = time.perf_counter() - start
        print(f'Время выполнения {func.__name__}: {work_time} сек.')
        return val
    return wrapper
