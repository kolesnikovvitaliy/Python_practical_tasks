def get_biggest(lst):
    if lst:
        return int(''.join(map(str, sorted(lst, key=lambda x: str(x)*10, reverse=True))))
        #return sorted(lst, key=lambda x: str(x)*10, reverse=True)
    return -1
   
print(get_biggest([9, 95, 982]))
#321
print(get_biggest([61, 228, 9, 3, 11]))
#961322811
print(get_biggest([7, 71, 72]))
print(get_biggest([]))
print(get_biggest([13, 221, 423, 53, 1, 2, 33, 58, 78554, 34, 65, 65, 2, 1]))
#78554656558534233433222211311
