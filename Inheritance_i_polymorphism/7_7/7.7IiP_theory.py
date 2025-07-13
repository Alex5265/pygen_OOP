def say(animal):
    return f'{animal.name} говорит {animal.sound()}'

class Cat:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return 'мяу'

class Dog:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return 'гав'


cat = Cat('Кемаль')
dog = Dog('Роджер')

for animal in (cat, dog):
    print(say(animal))