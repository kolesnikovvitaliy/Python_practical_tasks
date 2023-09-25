class Fibonacci:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        return self.a


# class Fibonacci:
#     def __init__(self):
#         self.two = self.one = 1
#         self.result = 0

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.result < 2:
#             self.result += 1
#             return 1
#         self.result = self.one + self.two
#         self.two = self.one
#         self.one = self.result
#         return self.result
