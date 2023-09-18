def recursion(n):
    if n < 0:
        print(n)
        return n
    print(n)
    recursion(n-5)
    print(n)