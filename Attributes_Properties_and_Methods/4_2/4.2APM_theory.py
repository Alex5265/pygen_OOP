class Cat:
    def say(self):
        print('Мяу')

    def eat(self):
        print('Мням')


cat = Cat()

cat.say()
cat.eat()

# Python преобразует в следующее:

class Cat:
    def say(self):
        print('Мяу')

    def eat(self):
        print('Мням')


cat = Cat()

Cat.say(cat)
Cat.eat(cat)

print()

cat1 = Cat()
cat2 = Cat()

cat1.say()
cat2.eat()
print()

class Cat:
    def say(self, sound):
        print(sound)

    def eat(self, meal):
        print(f'{meal} - это очень вкусно!')


cat1 = Cat()
cat2 = Cat()

cat1.say('Мяу')
cat1.eat('Молоко')

cat2.say('Мяяяу!')
cat2.eat('Рыба')
print()


class Cat:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

cat1 = Cat('Британский', 'Кемаль')
cat2 = Cat('Манчкин', 'Роджер')

print(cat1.breed, cat1.name)
print(cat2.breed, cat2.name)




