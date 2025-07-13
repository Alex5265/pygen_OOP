class Animal:
    def sound(self):
        pass

class Cat(Animal):
    def sound(self):
        return 'мяу'

class Dog(Animal):
    pass

class CatDog(Cat, Dog):
    pass


catdog = CatDog()

print(catdog.sound())