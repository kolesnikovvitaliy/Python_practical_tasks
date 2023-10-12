import re
item, text = [input() for _ in range(2)]
print(len(re.findall(fr'\b{item[:-2]}(ur|r)\b', text, re.I)))