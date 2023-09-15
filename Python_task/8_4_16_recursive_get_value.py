def get_value(data: (object | dict), key):
    if key in data:
        return data[key]

    for v in data.values():
        if isinstance(v, dict):
            value = get_value(v, key)
            if value is not None:
                return value
