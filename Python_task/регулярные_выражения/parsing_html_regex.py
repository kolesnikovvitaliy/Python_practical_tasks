import re
import sys

dict_tmp = {}
for item in sys.stdin.read().splitlines():
    match = re.findall(r'<([^>\/]+)>?', item)
    for i in match:
        if ' ' in i:
            match1 = (j for i in
                      re.findall(r'^(\w+)|(\w[\w-]*)=', i) for j in i if j)
            dict_tmp.setdefault(next(match1), []).append([j for j in match1])
        else:
            dict_tmp.setdefault(i, []).append('')
[print(*(f'{k}: {", ".join(sorted(set(j for i in v for j in i)))}'
         for k, v in dict(sorted(dict_tmp.items())).items()), sep="\n")]

# import re
# import sys

# text = sys.stdin.read()

# pattern = '<(\w+)( .*?)?>'
# tags = dict(re.findall(pattern, text))
# print(tags)
# for tag, atr in sorted(tags.items()):
#     print(f'{tag}:', ', '.join(sorted(re.findall(r'(?<= )\S+?(?==)', atr))))
