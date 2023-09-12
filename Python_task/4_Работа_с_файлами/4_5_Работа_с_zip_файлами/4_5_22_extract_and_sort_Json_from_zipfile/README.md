<h2 style="text-align:center">Шахматы были лучше</h2>

### Вам доступен архив data.zip, содержащий различные папки и файлы. Среди них есть несколько JSON файлов, каждый из которых содержит информацию о каком-либо футболисте:
```python
{
   "first_name": "Gary",
   "last_name": "Cahill",
   "team": "Chelsea",
   "position": "Defender"
}
```
#### У футболиста имеются следующие атрибуты: 

* first_name — имя
* last_name — фамилия
* team — название футбольного клуба
* position — игровая позиция
### Напишите программу, которая обрабатывает только данные JSON файлы и выводит имена и фамилии футболистов, выступающих за футбольный клуб Arsenal. Футболисты должны быть расположены в лексикографическом порядке имен, а при совпадении — в лексикографическом порядке фамилий, каждый на отдельной строке.

#### Примечание 1. Обратите внимание, что наличие у файла расширения .json не гарантирует, что он является корректным текстовым файлом в формате JSON. Для того чтобы определить, является ли файл корректным текстовым файлом в формате JSON, воспользуйтесь конструкцией try-except и функцией is_correct_json()


## Примеры решений:
* Первый вариант решения
```python
import json
from zipfile import ZipFile


file_name = 'data.zip'
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
```
* Второй вариант решения

```python

```


