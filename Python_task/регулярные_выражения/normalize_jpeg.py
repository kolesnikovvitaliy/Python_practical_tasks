import re


def normalize_jpeg(filename):
    return re.sub(r'\.\w+$', '.jpg', filename)

# r'(jpeg|jpg)$

print(normalize_jpeg('stepik.jPeG'))