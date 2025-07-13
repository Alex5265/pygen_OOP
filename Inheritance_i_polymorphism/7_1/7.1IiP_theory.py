# class Animal:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def sleep(self):
#         return f'{self.name} спит zZ'
#
# class Cat(Animal):
#     def __init__(self, name, age, eyecolor):
#         Animal.__init__(self, name, age)                   # вызываем инициализатор родительского класса
#         self.eyecolor = eyecolor
#
#     def sleep(self):
#         return f'{self.name} очень крепко спит zZ'
#
#     def jump(self):
#         return f'{self.name} прыгает!'
#
#
# cat = Cat('Кемаль', 1, 'желтый')
#
# print(cat.jump())



# class Animal:
#     en_name = 'animal'
#     ru_name = 'животное'
#
# class Cat(Animal):                         # наследует атрибуты родительского класса
#     pass
#
# class Dog(Animal):                         # переопределяет атрибуты родительского класса
#     en_name = 'dog'
#     ru_name = 'собака'
#
#
# print(Cat.en_name)
# print(Cat.ru_name)
# print(Dog.en_name)
# print(Dog.ru_name)


# class MyClass:
#    pass
#
#
# print(dir(MyClass()))
# print(dir(object()))


# class A:
#     pass
#
# class B(A):
#     pass
#
# class C(B):
#     pass
#
# print(object.__base__)
# print(A.__base__)
# print(B.__base__)
# print(C.__base__)



class A:
    pass

class B(A):
    pass

class C(B):
    pass


print('A, A',issubclass(A, A))
print('A, C',issubclass(A, C))
print('B, A',issubclass(B, A))
print('B, C',issubclass(B, C))
print('C, A',issubclass(C, A))
print('C, B',issubclass(C, B))
print()
print(issubclass(bool, int))
print(issubclass(int, bool))

print(isinstance(True, bool))
print(isinstance(True, int))







