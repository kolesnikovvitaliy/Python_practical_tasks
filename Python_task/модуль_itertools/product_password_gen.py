from itertools import product


def password_gen():
    for i, j, k in product(range(10), repeat=3):
        yield str(i) + str(j) + str(k)



passwords = password_gen()

print(next(passwords))
print(next(passwords))
print(next(passwords))
