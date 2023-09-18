def dict_travel(data: (object | dict), key=''):
    for k, v in sorted(data.items()):
        if isinstance(v, dict):
            dict_travel(v, key + f'{k}.')
        else:
            print(f'{key}{k}: {v}')