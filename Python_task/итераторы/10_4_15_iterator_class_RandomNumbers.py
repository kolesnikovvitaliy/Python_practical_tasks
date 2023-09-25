from random import randint


class RandomNumbers:
    def __init__(self, left, right, n):
        self.left = left
        self.right = right
        self.n = n
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == self.n:
            raise StopIteration
        value = randint(self.left, self.right)
        self.count += 1
        return value


# from random import randint

# class RandomNumbers:    
#     def __init__(self, left, right, n):
#         self.data = (randint(left, right) for _ in range(n))
        
#     def __iter__(self):
#         return self
    
#     def __next__(self):
#         return next(self.data)