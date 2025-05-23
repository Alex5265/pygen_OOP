# class MyClass:
#     pass
#
#
# obj = MyClass()
#
# print(obj)
# print(type(obj))
#
#
# print()
#
#
# class MyClass:
#     def __new__(cls, *args, **kwargs):
#         instance = object.__new__(cls)
#         return instance
#
#
# obj = MyClass()
#
# print(obj)
# print(type(obj))

# class Cat:
#     def __new__(cls, *args, **kwargs):
#         print('1. Создание экземпляра класса Cat')
#         instance = object.__new__(cls)
#         return instance
#
#     def __init__(self, name):
#         print('2. Инициализация созданного экземпляра класса Cat')
#         self.name = name
#
#
# cat = Cat.__new__(Cat)
# print(type(cat))
# print(cat.__dict__)
# Cat.__init__(cat, 'Кемаль')
#
# print(type(cat))
# print(cat.__dict__)

class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:                       # при первом вызове создаем объект
            cls._instance = object.__new__(cls)
        return cls._instance


first = Singleton()
second = Singleton()

print(first)
print(second)
print(first is second)


# Приведенный ниже код:

class MyClass:
    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        return instance

# равнозначен коду:

class MyClass:
    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        return instance

print()



class A(object):
    qux = 'A'

    def __init__(self, name):
        self.name = name

    def foo(self):
        print('foo')

class B(object):
    qux = 'B'

    def __init__(self):
        self.name = 'B object'

    def bar(self):
        print('bar')

a = A('a')

print(a.__dict__)
a.foo()
print(a.__class__)

a.__class__ = B

print(a.__class__)
print(a.__dict__)
a.bar()
print(a.qux)
