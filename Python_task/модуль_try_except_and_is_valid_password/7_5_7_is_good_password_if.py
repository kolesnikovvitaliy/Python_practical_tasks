def is_good_password(password):
    return all((
        len(password) >= 9,
        any(map(str.isdigit, password)),
        any(map(str.isupper, password)),
        any(map(str.islower, password)),
    ))