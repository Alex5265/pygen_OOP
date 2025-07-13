from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        print('Не определен')

    @abstractmethod
    def move(self):
        print('Животное движется')

class Cat(Animal):
    def sound(self):
        print('мяу')

    def move(self):
        super().move()
        print('Кот движется')


cat = Cat()

cat.move()
cat.sound()