# Класс RandomNumber
# Реализуйте класс RandomNumber, описывающий дескриптор, который при обращении к атрибуту возвращает случайное целое число в заданном диапазоне. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#
# start — целое число
# end — целое число
# cache — булево значение, по умолчанию равняется False
# Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.
#
# При обращении к атрибуту дескриптор должен возвращать случайное целое число от start до end включительно. Если в качестве значения параметра cache при создании дескриптора было указано значение True, при каждом обращении к атрибуту дескриптор должен возвращать то число, которое было сгенерировано при первом обращении.
#
# При установке или изменении значения атрибута дескриптор должен возбуждать исключение AttributeError с текстом:
#
# Изменение невозможно
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализации класса RandomNumber нет, она может быть произвольной.
from random import randint


class RandomNumber:
    def __init__(self, start, end, cache=False):
        self.start = start
        self.end = end
        if not cache:
            self.cache = cache
        else:
            self.cache = randint(self.start, self.end)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.cache:
            return self.cache
        return randint(self.start, self.end)

    def __set__(self, instance, value):
        raise AttributeError('Изменение невозможно')



class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

magicpoint = MagicPoint()

print(magicpoint.x in [1, 2, 3, 4, 5])
print(magicpoint.y in [1, 2, 3, 4, 5])
print(magicpoint.z in [1, 2, 3, 4, 5])

print()


class MagicPoint:
    x = RandomNumber(1, 5)
    y = RandomNumber(1, 5)
    z = RandomNumber(1, 5)

magicpoint = MagicPoint()

print(magicpoint.x in [6, 7, 8, 9, 10])
print(magicpoint.y in [6, 7, 8, 9, 10])
print(magicpoint.z in [6, 7, 8, 9, 10])

print()

class MagicPoint:
    x = RandomNumber(0, 5, True)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)

magicpoint = MagicPoint()
value = magicpoint.x

print(magicpoint.x in [0, 1, 2, 3, 4, 5])
print(magicpoint.x == value)
print(magicpoint.x == value)
print(magicpoint.x == value)

print()

class MagicPoint:
    x = RandomNumber(0, 5)
    y = RandomNumber(0, 5)
    z = RandomNumber(0, 5)

magicpoint = MagicPoint()

try:
    magicpoint.x = 10
except AttributeError as e:
    print(e)






