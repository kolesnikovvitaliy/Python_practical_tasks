def tribonacci(n):
    history = {1: 1, 2: 1, 3: 1}

    def recursion(n):
        if n in history:
            return history[n]
        else:
            res = recursion(n - 3) + recursion(n - 2) + recursion(n - 1)
            history[n] = res
        return history[n]
    return recursion(n)
