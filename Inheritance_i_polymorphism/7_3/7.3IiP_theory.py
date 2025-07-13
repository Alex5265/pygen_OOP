# class Cat:
#     pass
#
#
# print('__new__' in dir(Cat))
# print('__init__' in dir(Cat))

# class Cat:
#     def __new__(cls, *args, **kwargs):
#         print('1. Вызов метода __new__()')
#         print(cls)
#         return super().__new__(cls)
#
#     def __init__(self, name):
#         print('2. Вызов метода __init__()')
#         self.name = name
#         print(self)
#
#     def __repr__(self):
#         return f'Cat({repr(self.name)})'
#
#
# cat = Cat('Кемаль')
# print()

# class Animal:
#     pass
#
# class Cat:
#     def __new__(cls, *args, **kwargs):
#         print('1. Вызов метода __new__()')
#         return Animal()
#
#     def __init__(self, name):
#         print('2. Вызов метода __init__()')
#         self.name = name
#
#
# cat = Cat('Кемаль')

# class Distance(float):
#     def __init__(self, value, unit):
#         super().__init__()
#         self.unit = unit
#
#
# distance = Distance(1, 'Meters')
#
# print(distance)
# print(distance.unit)
# print()

# class Distance(float):
#     def __new__(cls, value, unit):
#         instance = super().__new__(cls, value)
#         instance.unit = unit
#         return instance


# distance = Distance(1, 'Meters')
#
# print(distance)
# print(distance.unit)
# print()
#
#
# distance = Distance(1, 'Meters')
# print(distance, distance.unit)
#
# distance.unit = 'Kilometers'
# print(distance, distance.unit)


# class WordCountString(str):
#     def __str__(self):
#         return f'{super().__str__()}, {self.words()}'
#
#     def words(self):
#         return len(self.split())
#
#
# wordcountstring = WordCountString('I Love Beegeek')
#
# print(wordcountstring.words())
# print(wordcountstring)

# class Distance(float):
#     def __new__(cls, value, unit):
#         instance = super().__new__(cls, value)
#         instance.unit = unit
#         return instance
#
#     def print_self(self):
#         print(self)
#
#
# n = Distance(4, 'km')
# n.print_self()  # 4.0


class Distance(float):
    def __init__(self, value):
        super().__init__()
        self.unit = 'Meter'


distance = Distance(1)

print(distance)
print(distance.unit)
print()

class Distance(float):
    def __new__(cls, value, unit):
        return super().__new__(cls, value)

    def __init__(self, value, unit):
        super().__init__()
        self.unit = unit


distance = Distance(1, 'Meters')

print(distance)         # 1.0
print(distance.unit)    # Meters




