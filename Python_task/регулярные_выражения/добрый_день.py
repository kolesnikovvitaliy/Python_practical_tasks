# import re


# a = input()
# flag = False
# text = ['Здравствуйте', 'Доброе утро', 'Добрый день', 'Добрый вечер']


# for i in text:
#     if re.match(i, a, re.IGNORECASE):
#         flag = True
#         break

# print(flag)
import re
print(bool(re.search(r'^Здравствуйте|^Доброе утро|^Добрый (день|вечер)', input(), re.I)))