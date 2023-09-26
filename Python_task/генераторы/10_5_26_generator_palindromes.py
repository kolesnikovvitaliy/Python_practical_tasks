def palindromes():
    i = 1
    while True:
        if i == int(str(i)[::-1]):
            yield i
        i += 1
