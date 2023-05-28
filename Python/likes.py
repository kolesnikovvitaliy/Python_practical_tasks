def likes(my_list):

    result = ("'Никто не оценил данную запись'",
                "f'{my_list[0]} оценил(а) данную запись'",
                "f'{my_list[0]} и {my_list[1]} оценили данную запись'",
                "f'{my_list[0]}, {my_list[1]} и {my_list[2]} оценили данную запись'",
                "f'{my_list[0]}, {my_list[1]} и {len(my_list) - 2} других оценили данную запись'")
    
    return eval(result[len(my_list)] if len(my_list) <= 3 else result[-1])

print(likes(['Тимур', 'Артур', 'Руслан', 'Анри', 'a', 'b']))
print(likes(['Тимур', 'Артур', 'Руслан', 'Анри']))
print(likes(['Тимур', 'Артур', 'Руслан']))
print(likes(['Тимур', 'Артур']))
print(likes(['Тимур']))
print(likes([]))