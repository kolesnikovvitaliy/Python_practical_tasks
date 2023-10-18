import re
import sys

regex = r't=[0-9\.\+]+\b'
if (key := re.search(regex, sys.stdin.read())):
    print(key.group())