def get_min_max(data):
    if not data:
        return
    return data.index(min(data)), data.index(max(data))
