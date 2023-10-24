from collections import OrderedDict


def custom_sort(ordered_dict, by_values=False):
    if not by_values:
        [ordered_dict.move_to_end(key) for key in sorted(ordered_dict)]
    else:
        [ordered_dict.move_to_end(i[0])
         for i in sorted(ordered_dict.items(), key=lambda x: x[1])]


data = OrderedDict(Earth=3, Mercury=1, Mars=4, Venus=2)
custom_sort(data, by_values=True)

print(*data.items())
# ('Mercury', 1) ('Venus', 2) ('Earth', 3) ('Mars', 4)
# data = OrderedDict(Dustin=29, Anabel=17, Brian=40, Carol=16)
# custom_sort(data)

# print(data)
# # OrderedDict([('Anabel', 17), ('Brian', 40), ('Carol', 16), ('Dustin', 29)])