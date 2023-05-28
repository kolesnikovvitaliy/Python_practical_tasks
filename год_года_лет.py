def choose_plural(n, string):
    if (n // 10) % 10 != 1:
        if n % 10 == 1:
            return f'{n} {string[0]}'
        elif (n % 10) in (2,3,4):
            return f'{n} {string[1]}'
    return f'{n} {string[2]}'
    # get_suffix(age):   
    # year = "лет" 
    # if (age // 10) % 10 != 1:
    #     if age % 10 == 1:
    #         year = "год"
    #     elif (age % 10) in (2,3,4):
    #         year = "года"
    # return f'{integer}   '
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))
print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(21, ('пример', 'примера', 'примеров')))