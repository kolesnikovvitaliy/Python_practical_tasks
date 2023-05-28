import time
 
def for_and_append():                            # с использованием цикла for и метода append()
    iterations = 10_000_000
    result = []
    for i in range(iterations):
        result.append(i + 1)
    return result
        

def list_comprehension():                        # с использованием списочного выражения
    iterations = 10_000_000
    return [i + 1 for i in range(iterations)]


def get_the_fastest_func(funcs):
    a = {}
    for i in range(len(funcs)):
        start = time.perf_counter()
        funcs[i]()
        stop = time.perf_counter()
        a.setdefault((stop-start),funcs[i].__name__)
    return a
    

funcs = [list_comprehension, for_and_append]

print(get_the_fastest_func(funcs))