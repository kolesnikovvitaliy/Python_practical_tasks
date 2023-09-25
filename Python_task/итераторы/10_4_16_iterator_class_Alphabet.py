class Alphabet:
    def __init__(self, language):
        __data = {'en': range(97, 123), 'ru': range(1072, 1104)}
        self.count = 0
        self.text = [chr(i) for i in __data[language]]

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == len(self.text):
            self.count = 0
        value = self.text[self.count]
        self.count += 1
        return value
