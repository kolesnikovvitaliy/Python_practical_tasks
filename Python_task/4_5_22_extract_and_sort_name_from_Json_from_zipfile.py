# Первое решение
import json
from zipfile import ZipFile


file_name = './task_files/data.zip'
key = 'team'
value = 'Arsenal'
key_item_1 = 'first_name'
key_item_2 = 'last_name'


def is_correct_json(data: object, key: str, value: str):
    try:
        tmp = json.load(data)
        if tmp[key] == value:
            return tmp
    except Exception:
        return


def extract(file_name: ZipFile, key: str, value: str) -> list:
    _lst = []
    with ZipFile(file_name) as zip_file:
        for items in zip_file.infolist():
            if not items.is_dir() and items.filename.endswith('.json'):
                with zip_file.open(items.filename) as data:
                    item = is_correct_json(data, key, value)
                    if item:
                        _lst.append(item)
    return _lst


def get_sort_name(file_name: ZipFile,
                  key: str,
                  value: str,
                  key_item_1: str,
                  key_item_2: str) -> str:
    _tmp = sorted(extract(file_name, key, value),
                  key=lambda x: (x[key_item_1], x[key_item_2]))
    for item in _tmp:
        print(f'{item[key_item_1]} {item[key_item_2]}')


get_sort_name(file_name, key, value, key_item_1, key_item_2)


# Второе решение

import json as js


with __import__('zipfile').ZipFile('./task_files/data.zip') as zf:
    l = []
    for i in zf.infolist():
        if not i.is_dir() and i.filename.endswith('.json'):
            zf.extract(i)
            try:
                with open(i.filename, encoding='utf-8') as file:
                    p = js.load(file)
                    if p['team'] == 'Arsenal':
                        l.append((p['first_name'], p['last_name']))
            except:
                continue

[print(*i) for i in sorted(l)]