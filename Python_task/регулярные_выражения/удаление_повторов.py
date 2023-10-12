import re

TEXT = 'beegeek,beegeek,beegeek! python python.. Python.. stepik?stepik?stepik'

print(re.sub(r'\b(\w+)(?:\W+\1\b)+', r'\1', TEXT))