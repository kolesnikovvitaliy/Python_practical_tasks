def new_func(file_name):
    try:
        file = open(file_name, encoding='utf-8')
        try:
            text = file.read()
            print(text)
        finally:
            file.close()
    except FileNotFoundError:
        print('Файл с указанным именем не найден!')