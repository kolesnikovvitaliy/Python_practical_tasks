def dict_travel(data: (object | dict), key=''):
    for k, v in sorted(data.items()):
        print(k, v)
        if isinstance(v, dict):
            dict_travel(v, key + f'{k}.')
        else:
            print(f'{key}{k}: {v}')