def linear(data):
    _lst = []

    def recursion(data):
        if data is None:
            return 0
        if type(data) == int:
            _lst.append(data)
        elif type(data) == list:
            for i in data:
                recursion(i)
    recursion(data)
    return _lst
