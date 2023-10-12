import re

TEXT = input()
while re.findall(r'(\(|\))', TEXT):
    TEXT = re.sub(r'(\d+)\({1}(\w+)\){1}',
                  lambda x: x.group(2) * int(x.group(1)), TEXT)
print(TEXT)
