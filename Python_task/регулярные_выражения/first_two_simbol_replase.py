import re


print(re.sub(r'\b(\w)(\w)', r'\2\1', input()))