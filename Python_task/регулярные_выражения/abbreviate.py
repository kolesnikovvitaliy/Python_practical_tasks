import re


# def abbreviate(phrase):
#     return ''.join(item.upper() for items in
#                    re.findall(r'(\w)\w*([A-Z])\w*|(\w)\w*',
#                               phrase) for item in items if item)


def abbreviate(phrase):
    return ''.join(re.findall(r'[A-Z]|\b\w', phrase)).upper()


print(abbreviate('JS game sec'))
print(abbreviate('javaScript object notation'))
print(abbreviate('frequently asked questions'))