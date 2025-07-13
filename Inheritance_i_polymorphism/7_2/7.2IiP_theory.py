# class Animal:
#     def __init__(self, name, age):
#         self.name = name                               # имя животного
#         self.age = age                                 # возраст животного
#
#     def sleep(self):
#         return f'{self.name} спит zZ'
#
# class Cat(Animal):
#     def sleep(self):
#         return f'{self.name} очень крепко спит zZ'
#
#     def sound(self):
#         return 'Мяу!'


# class Animal:
#     def __init__(self, name, age, eyecolor):
#         self.name = name
#         self.age = age
#         self.eyecolor = eyecolor
#
# class Cat(Animal):
#     def __init__(self, name, age, eyecolor, breed):
#         Animal.__init__(self, name, age, eyecolor)
#         self.breed = breed
#
#
# animal = Animal('Роджер', 2, 'черный')
# cat = Cat('Кемаль', 1, 'синий', 'манчкин')
#
# print(animal.name, animal.age, animal.eyecolor)
# print(cat.name, cat.age, cat.eyecolor, cat.breed)


# class Rectangle:
#     def __init__(self, length, width):
#         self.length = length
#         self.width = width
#
# class Square(Rectangle):
#     def __init__(self, side):
#         Rectangle.__init__(self, side, side)
#
#
# rectangle = Rectangle(3, 4)
# square = Square(2)
#
# print(rectangle.length, rectangle.width)
# print(square.length, square.width)

# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# class Cat(Animal):
#     def __init__(self, name, age, breed):
#         super().__init__(name, age)                    # неявно обращаемся к методу __init__() родительского класса
#         self.breed = breed
#
# cat = Cat('Кемаль', 1, 'манчкин')
#
# print(cat.name, cat.age, cat.breed)


# class Animal:
#     def __init__(self, name):
#         print('Вызов метода __init__() класса Animal')
#         self.name = name
#
# class Cat(Animal):
#     pass
#
# class Kitten(Cat):
#     def __init__(self, name, breed):
#         print('Вызов метода __init__() класса Kitten')
#         super().__init__(name)
#         self.breed = breed
#
#
# cat = Kitten('Кемаль', 'манчкин')
#
# print(cat.name, cat.breed)

class Animal:
    def __init__(self, name):
        self.name = name

class Cat(Animal):
    def sound(self):
        return 'мяу'

    def info(self):
        return f'Имя: {self.name}, звук: {self.sound()}'

class Dog(Animal):
    def sound(self):
        return 'гав'

    def info(self):
        return f'Имя: {self.name}, звук: {self.sound()}'


cat = Cat('Кемаль')
dog = Dog('Роджер')

print(cat.info())
print(dog.info())



















