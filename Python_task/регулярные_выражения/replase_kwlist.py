import re
import keyword

STR_KWLIST = ','.join(keyword.kwlist)


def replase_kwlist(string_math):
    text = string_math.group(0)
    if re.findall(fr'\b{text}\b', STR_KWLIST, re.I):
        return '<kw>'
    return text


print(re.sub(r'\w+\'?\w?', replase_kwlist, input()))


# import re
# import keyword

# keys = '|'.join(keyword.kwlist)

# print(re.sub(fr"\b({keys})\b", r'<kw>', input(), flags=re.I))
