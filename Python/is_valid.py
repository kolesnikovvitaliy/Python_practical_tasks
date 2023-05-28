def is_valid(pin):
    return pin.isdigit() and len(pin) in range(4,7)
print(is_valid('921341'))