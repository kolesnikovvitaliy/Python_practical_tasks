import re
import sys

text = sys.stdin.read()
text = re.sub(r'(?ms) *(\"{3}).*?\1\n', '', text)
text = re.sub('(?m)(^ *#.*?$\n)|( *#.*?$)', '', text)
print(text)

# (?ms)\s*(\"{3}).*?\1|\n#.*?$|\n? *#.*?$