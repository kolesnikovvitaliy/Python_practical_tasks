import re


def normalize_whitespace(string):
    return re.sub(r'\s{2,}', ' ', string)


print(normalize_whitespace('AAAA                A                AAAA'))