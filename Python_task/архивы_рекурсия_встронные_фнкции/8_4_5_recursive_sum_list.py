def recursive_sum(data):
    result_sum = 0
    if data is None:
        return 0
    if type(data) == int:
        result_sum += data
    elif type(data) == list:
        for i in data:
            result_sum += recursive_sum(i)
    return result_sum

# def recursive_sum(numbers):
#     if type(numbers) == int:
#         return numbers
#     s = sum([recursive_sum(i) for i in numbers])
#     return s