import re


def multiple_split(string, delimiters):
    return re.split(fr'(?:{"|".join(map(re.escape, delimiters))})', string)
