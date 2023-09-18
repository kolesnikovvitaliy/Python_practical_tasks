def to_binary(number):
    res = ''
    if number == 0:
        return '0'

    def recursion(number, res):
        if number == 0:
            return res
        res = str(number % 2) + res
        return recursion(number // 2, res)
    return recursion(number, res)

# def to_binary(number):
#     if number <= 1:
#         return str(number)
#     return to_binary(number // 2) + str(number % 2)