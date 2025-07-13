# Класс AdvancedTuple
# Реализуйте класс AdvancedTuple, наследника класса tuple, который описывает кортеж, умеющий выполнять операцию сложения (+, +=) не только с экземплярами классов AdvancedTuple и tuple, но и с любыми итерируемыми объектами. Процесс создания экземпляра класса AdvancedTuple должен совпадать с процессом создания экземпляра класса tuple.
#
# Примечание 1. Как бы ни выполнялось сложение, с помощью оператора + или +=, результатом операции должен являться новый экземпляр класса AdvancedTuple.
#
# Примечание 2. Никаких ограничений касательно реализации класса AdvancedTuple нет, она может быть произвольной.

class AdvancedTuple(tuple):
    def __add__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(self) + tuple(other))
        return NotImplemented

    def __radd__(self, other):
        if hasattr(other, '__iter__'):
            return AdvancedTuple(tuple(other) + tuple(self))
        return NotImplemented







advancedtuple = AdvancedTuple([1, 2, 3])

print(advancedtuple + (4, 5))
print(advancedtuple + [4, 5])
print({'a': 1, 'b': 2} + advancedtuple)
print()


advancedtuple = AdvancedTuple([1, 2, 3])

advancedtuple += [4, 5]
advancedtuple += iter([6, 7, 8])
print(advancedtuple)
print(type(advancedtuple))

















