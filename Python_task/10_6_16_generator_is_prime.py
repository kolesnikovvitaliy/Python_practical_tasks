def is_prime(number):
    if number == 1:
        return False
    return not sum(number % i == 0 for i in range(2, (number//2)+1))
