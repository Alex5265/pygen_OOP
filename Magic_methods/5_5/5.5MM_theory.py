class PiggyBank:
    def __init__(self, coins):
        self.coins = coins

    def __repr__(self):
        return f'PiggyBank({self.coins})'

    def __add__(self, other):
        return PiggyBank(self.coins + other)

    def __radd__(self, other):
        print('Вызов метода __radd__()')
        return self.__add__(other)


bank = PiggyBank(10)
num = 5

print(num.__add__(bank))