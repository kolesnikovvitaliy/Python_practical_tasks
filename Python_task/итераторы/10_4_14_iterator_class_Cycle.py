class Cycle:
    def __init__(self, iterable):
        self.iterble = iterable
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.iterble):
            self.count = 0
        value = self.iterble[self.count]
        self.count += 1
        return value
