def sandwich(func):
    def wrapper(*args, **kwargs):
        print('---- Верхний ломтик хлеба ----')
        result_func = func(*args, **kwargs) 
        print('---- Нижний ломтик хлеба ----')
        return result_func
    return wrapper



# @sandwich
# def add_ingredients(ingredients):
#     print(' | '.join(ingredients))

# add_ingredients(['томат', 'салат', 'сыр', 'бекон'])