def polynom(x):
    func = x**2 + 1
    if hasattr(polynom, 'values'):
        polynom.__dict__['values'].add(func)
    else:
        polynom.__setattr__('values', set())
        polynom.values.add(func)
    return func
