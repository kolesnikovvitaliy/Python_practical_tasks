# Первое решение
from zipfile import ZipFile


def size(in_bytes: int):
    table = {1: 'B', 1024: 'KB', 1048576: 'MB', 1073741824: 'GB'}
    for key, val in sorted(table.items(), reverse=True):
        if in_bytes > key:
            return round(in_bytes / key), val


def get_file_and_indent(items):
    dir = [i for i in items.filename.split('/') if i != '']
    indent = len(dir)-1
    return dir, indent


with ZipFile('.task_files/desktop.zip') as zip_file:
    for items in zip_file.infolist():
        if items.is_dir():
            file_name, indent = get_file_and_indent(items)
            print(f'{"  "*indent}{file_name[-1]}')
        else:
            file_name, indent = get_file_and_indent(items)
            file_size = ' '.join(map(str, size(items.file_size)))
            print(f'{"  "*indent}{file_name[-1]} {file_size}')

# Второе решение


def size(byt: int):
    d = {1024 ** 3: 'GB', 1024 ** 2: 'MB', 1024: 'KB', 1: 'B'}
    for key, val in d.items():
        if byt > key:
            return round(byt / key), val


with __import__('zipfile').ZipFile('.task_files/desktop.zip') as zip_file:
    for i in zip_file.infolist():
        p = i.filename.rstrip('/').split('/')
        print(f"{'  ' * (len(p) - 1)}{p[-1]}", *size(i.file_size) or '')
