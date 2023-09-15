def get_all_values(data: (object | dict), key: str):
    velue_set = set()

    def recursion(data, key):
        if key in data:
            velue_set.add(data[key])

        for v in data.values():
            if isinstance(v, dict):
                value = recursion(v, key)
                if value is not None:
                    return value

    recursion(data, key)
    return velue_set
