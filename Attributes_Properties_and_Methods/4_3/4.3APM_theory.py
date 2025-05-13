class PiggyBank:
    def __init__(self, balance=0, volume =400):
        self.balance = balance
        self.volume = volume

    def add_coins(self, coins):
        if self.balance + coins > self.volume:
            print('Копилка слишком мала')
        else:
            self.balance += coins

    def remove_coins(self, coins):
        if self.balance - coins < 0:
            print('В копилке недостаточно монет')
        else:
            self.balance -= coins



piggybank = PiggyBank(0, 10)

print(piggybank.balance)

piggybank.remove_coins(20)                            # пробуем из пустой копилки вынуть 20 монет
piggybank.add_coins(20)                               # пробуем добавить избыточное количество монет

print(piggybank.balance)

