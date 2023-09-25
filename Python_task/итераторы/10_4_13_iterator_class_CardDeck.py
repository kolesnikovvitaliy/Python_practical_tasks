class CardDeck:
    def __init__(self):
        self.suits = ['пик', 'треф', 'бубен', 'червей']
        self.ranks = [i for i in range(2, 11)] + ['валет', 'дама', 'король', 'туз']
        self.card = iter([f'{j} {i}' for i in self.suits for j in self.ranks])

    def __iter__(self):
        return self

    def __next__(self):
        return next(self.card)
