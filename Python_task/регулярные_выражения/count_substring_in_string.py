import re
text, item = [input() for _ in range(2)]
print(len(re.findall(fr'\B({item})\B', text, re.I)))
####################################################
import re
text, item = [input() for _ in range(2)]
print(len(re.findall(fr'\b({item})\b', text)))