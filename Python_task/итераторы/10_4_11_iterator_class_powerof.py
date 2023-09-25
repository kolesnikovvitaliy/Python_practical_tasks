class PowerOf:
    def __init__(self, number):
        self.number = number
        self.raise_to_a_power = 0

    def __iter__(self):
        return self

    def __next__(self):
        value = self.number ** self.raise_to_a_power
        self.raise_to_a_power += 1
        return value
