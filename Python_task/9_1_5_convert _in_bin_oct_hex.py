def convert(n):
    return f'{n:b}', f'{n:o}', f'{n:X}'


# def convert(num):
#     funcs = (bin, oct, hex)
#     prefix = ('0b', '0o', '0x')
#     result = []

#     for index, func in enumerate(funcs):
#         pref = [prefix[index], '-' + prefix[index]][num < 0]
#         item = [str(func(num)).removeprefix(pref),
#                 '-' + str(func(num)).removeprefix(pref)][num < 0]
#         result.append(item)
#     result.append(result.pop().upper())

#     return tuple(result)