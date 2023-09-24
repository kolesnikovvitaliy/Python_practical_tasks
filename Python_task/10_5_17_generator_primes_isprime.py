def primes(left, right):
    def isprime(n):
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return d * d > n
    for i in range(left, right+1):
        if isprime(i) and i != 1:
            yield i
