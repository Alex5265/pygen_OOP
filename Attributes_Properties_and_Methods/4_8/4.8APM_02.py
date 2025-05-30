# Класс Negator
# Реализуйте класс Negator. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Класс Negator должен иметь один статический метод:
#
# neg() — метод, принимающий в качестве аргумента объект и возвращающий его противоположное значение. Если методу передается целое или вещественное число, он должен возвращать это число, взятое с противоположным знаком. Если методу в качестве аргумента передается булево значение, он должен возвращать булево значение, противоположное переданному. Если переданный объект принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
# Аргумент переданного типа не поддерживается
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализации класса Negator нет, она может быть произвольной.
from functools import singledispatchmethod


class Negator:
    @singledispatchmethod
    @staticmethod
    def neg(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @neg.register(float)
    @neg.register(int)
    @staticmethod
    def _numerick_neg(data):
        return data * -1

    @neg.register(bool)
    @staticmethod
    def _bool_neg(data):
        return not data

print(Negator.neg(11.0))
print(Negator.neg(-12))
print(Negator.neg(True))
print(Negator.neg(False))

print()

try:
    Negator.neg('number')
except TypeError as e:
    print(e)




