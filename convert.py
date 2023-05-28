# def convert(string):
#     count_1 = 0
#     count_2 = 0
#     for i in string:
#         if i.isdigit():
#             break
#         else:
#             if i.isupper():
#                 count_1 += 1
#             else:
#                 count_2 += 1
#     if count_1 > count_2:
#         return string.upper()
#     else:
#         return string.lower()
def convert(string):
    if sum(1 if c.isupper() else -1 for c in string if c.isalpha()) > 0:
        return string.upper()
    return string.lower()  
#print(convert('pyTHON'))
#print(convert('BEEgeek'))
#print(convert('pi31415!'))
print(convert('PIIIpiii'))