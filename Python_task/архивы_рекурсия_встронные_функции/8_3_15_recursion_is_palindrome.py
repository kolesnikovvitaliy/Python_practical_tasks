def is_palindrome(string):
    if not string or len(string) == 1:
        return True
    elif string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    return False