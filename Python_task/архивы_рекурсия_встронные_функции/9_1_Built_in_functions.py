films = {'Spider-Man: No Way Home': {'imdb': 8.8, 'kinopoisk': 8.3},
         'Don"t Look Up': {'imdb': 7.3, 'kinopoisk': 7.6}}

print(min(films, key=lambda x: sum(films[x].values())))  ## func - min
#############################################################################
def non_negative_even(numbers):
    return all(map(lambda x: x % 2 == 0 and x >= 0, numbers))  ## func - all
#############################################################################
def is_greater(lists, number):
    return any(sum(i) > number for i in lists)  ## func - any
#############################################################################
def custom_isinstance(objects: object, typeinfo: (type, tuple)):
    return sum([1 for i in objects if isinstance(i, typeinfo)])  ## func - isinstance
#############################################################################
numbers = [-7724, 5023, 3197, -102]
print(numbers.index(max(numbers)))  ## func - max
##############################################################################
def my_pow(number):
    return sum(int(v)**k for k, v in enumerate(str(number), 1))  ## func - enumerate
################################################################################
for i in sorted(zip(names, map(lambda x, y: x-y, box_offices, budgets))):
    print(f'{i[0]}: {i[1]}$')  ## func - zip, lambda
################################################################################
def zip_longest(*args, fill=None):
    return [*zip(*[i + [fill] * (max(map(len, args)) - len(i)) for i in args])]   ## func - zip
################################################################################
print(''.join(sorted(input(), key=lambda x: (x in '24680', x.isdigit(), x.isupper(), x))))   ## func - filter, sort
# string = input()
# sort_is_lower = list(sorted(filter(lambda x: x.isalpha() and x.islower(), string)))
# sort_is_upper = list(sorted(filter(lambda x: x.isalpha() and x.isupper(), string)))
# srot_is_digit_even = list(sorted(filter(lambda x: x.isdigit() and int(x) % 2 == 0, string)))
# sort_is_digit_odd_number = list(sorted(filter(lambda x: x.isdigit() and int(x) % 2 != 0, string)))
# print(''.join([*sort_is_lower, *sort_is_upper, *sort_is_digit_odd_number, *srot_is_digit_even]))
