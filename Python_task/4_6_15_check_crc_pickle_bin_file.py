import sys
import pickle

file_name, item = [item.rstrip() for item in sys.stdin.readlines()]
item = int(item)


def extract_pickle_file(file_name: str):
    with open(file_name, mode='rb') as file:
        obj = pickle.load(file)
    return obj


def csum(obj: (list | dict)):
    _lst = list(filter(lambda x: isinstance(x, int), obj)) or [0]
    return [sum(_lst), max(_lst)*min(_lst)][isinstance(obj, list)]


def result_item_and_csum(file_name: object, item: int):
    obj = extract_pickle_file(file_name)

    if item == csum(obj):
        print('Контрольные суммы совпадают')
    else:
        print('Контрольные суммы не совпадают')


if __name__ == "__main__":
    result_item_and_csum(file_name, item)
