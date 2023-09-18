def verification(login: str, password: str, success: object, failure: object):
    import re
    _excepts = {1: 'буквы', 2: 'заглавной буквы',
                3: 'строчной буквы', 4: 'цифры'}

    _checks = {1: password.isdigit() or not re.findall(r'[a-zA-Z]', password),
               2: not re.findall(r'[A-Z]+', password),
               3: not re.findall(r'[a-z]+', password),
               4: not re.findall(r'[0-9]+', password)
               }

    if any(_checks.values()):
        key_except = min(map(lambda x: x[0],
                             filter(lambda x: x[1] is True, _checks.items())))
        return failure(login,
                       f'в пароле нет ни одной {_excepts.get(key_except)}')
    else:
        return success(login)