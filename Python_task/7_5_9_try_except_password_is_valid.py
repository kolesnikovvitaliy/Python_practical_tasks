import sys


class PasswordError(Exception):
    pass


class LengthError(PasswordError):
    pass


class LetterError(PasswordError):
    pass


class DigitError(PasswordError):
    pass


def is_good_password(password: str):
    try:
        password[8]
    except Exception:
        raise LengthError
    try:
        tuple(filter(str.isupper, password))[0]
        tuple(filter(str.islower, password))[0]
    except Exception:
        raise LetterError
    try:
        tuple(filter(str.isdigit, password))[0]
    except Exception:
        raise DigitError
    return True


passwords = [word.rstrip() for word in sys.stdin]

for item in passwords:
    try:
        is_good_password(item)
    except Exception as err:
        print(type(err).__name__)
    else:
        print('Success!')
        break
