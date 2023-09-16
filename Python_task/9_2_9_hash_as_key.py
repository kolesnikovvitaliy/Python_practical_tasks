def hash_as_key(objects):
    dict_hash_key = {}
    [dict_hash_key.setdefault(hash(k), []).append(k) for k in objects]
    for k, v in dict_hash_key.items():
        if len(v) <= 1:
            dict_hash_key[k] = v[0]
    return dict_hash_key


data = [11, 22, 33, 44, 55, 66, 77, 88, 99, 111]

print(hash_as_key(data))