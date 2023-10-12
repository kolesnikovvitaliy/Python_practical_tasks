import re
import sys 


for item in sys.stdin.read().splitlines():
    match = re.findall(r'(?<=href=\")(.+)\">(.+)</a>', item)
    if match:
        print(', '.join(*match))