class Xrange:
    def __init__(self, start, end, step=1):
        self.start = start-step
        self.end = end
        self.step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self.step > 0 and self.start >= self.end-self.step:
            raise StopIteration
        elif self.step < 0 and self.start <= self.end-self.step:
            raise StopIteration
        self.start += self.step
        return self.start
