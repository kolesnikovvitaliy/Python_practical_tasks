import re
import sys

regex = r'(?<=Activation key: )([a-zA-Z0-9]{5}-?)+(?!\S)'
if (key := re.search(regex, sys.stdin.read())):
    print(key.group())