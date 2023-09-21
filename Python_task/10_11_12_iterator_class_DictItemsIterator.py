class DictItemsIterator:
    def __init__(self, data: dict):
        self.data = data
        self.stop = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.stop == len(self.data):
            raise StopIteration
        value = list(map(lambda x: (x, self.data[x]), self.data))[self.stop]
        self.stop += 1
        return value


# class DictItemsIterator:
#     def __init__(self, data):
#         self.data = data
#         self.keys = iter(data)

#     def __iter__(self):
#         return self

#     def __next__(self):
#         key = next(self.keys)
#         return key, self.data[key]