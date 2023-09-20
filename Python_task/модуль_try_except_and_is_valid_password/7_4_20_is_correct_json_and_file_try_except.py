import json


def is_correct_json(data):
    try:
        tmp = json.load(data)
        print(tmp)
    except Exception:
        print('Ошибка при десериализации')


try:
    with open(input(), encoding='UTF-8') as file:
        is_correct_json(file)
except Exception:
    print('Файл не найден')