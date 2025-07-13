# Класс BitArray
# Реализуйте класс BitArray, описывающий битовый список, то есть список, элементами которого являются только нули и единицы. При создании экземпляра класс должен принимать один аргумент:
#
# iterable — итерируемый объект, определяющий начальный набор элементов битового списка. Если не передан, начальный набор считается пустым
# Экземпляр класса BitArray должен иметь следующее неформальное строковое представление:
#
# [<первый элемент битового списка>, <второй элемент битового списка>, ...]
# При передаче экземпляра класса BitArray в функцию len() должно возвращаться количество элементов в нем. При передаче экземпляра класса BitArray в функцию reversed() должен возвращаться итератор, элементами которого являются элементы переданного экземпляра класса BitArray , расположенные в обратном порядке.
#
# Экземпляр класса BitArray должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
#
# Помимо этого, экземпляр класса BitArray должен поддерживать операцию проверки на принадлежность с помощью оператора in.
#
# Также экземпляр класса BitArray должен позволять получать значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.
#
# Вдобавок ко всему, экземпляр класса BitArray должен поддерживать унарный оператор ~, выполняющий операцию логического отрицания для каждого бита битового списка, тем самым преобразуя 0 в 1, а 1 в 0. Результатом работы оператора должен являться новый экземпляр класса BitArray.
#
# Наконец, экземпляры класса BitArray должны поддерживать между собой логические операции с помощью операторов & и |:
#
# оператор & должен выполнять операцию логического И над каждой парой битов двух битовых списков равной длины. Результатом работы оператора должен являться новый экземпляр класса BitArray
#
# оператор | должен выполнять операцию логического ИЛИ над каждой парой битов двух битовых списков равной длины. Результатом работы оператора должен являться новый экземпляр класса BitArray
#
# Примечание 1. Перед решением подумайте, какой абстрактный класс из модуля collections.abc будет удобен в качестве родительского.
#
# Примечание 2. Экземпляр класса BitArray не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса BitArray измениться  не должен.
#
# Примечание 3. Если объект, с которым выполняется логическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
#
# Примечание 4. Никаких ограничений касательно реализации класса BitArray нет, она может быть произвольной.



from collections.abc import Sequence


class BitArray(Sequence):
    def __init__(self, iterable=()):
        self._data = list(iterable)

    def __str__(self):
        return str(self._data)

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        if isinstance(index, (int, slice)):
            return self._data[index]
        return NotImplemented

    def __invert__(self):
        return __class__(int(not item) for item in self._data)

    def __or__(self, other):
        if isinstance(other, __class__) and len(self) == len(other):
            return __class__(self_item | other_item for self_item, other_item in zip(self._data, other._data))
        return NotImplemented

    def __and__(self, other):
        if isinstance(other, __class__) and len(self) == len(other):
            return __class__(self_item & other_item for self_item, other_item in zip(self._data, other._data))
        return NotImplemented



bitarray = BitArray([1, 0, 1, 1])

print(bitarray)
print(~bitarray)
print(bitarray[0])
print(bitarray[1])
print(bitarray[-1])
print(0 in bitarray)
print(1 not in bitarray)
print()

bitarray1 = BitArray([1, 0, 1, 1])
bitarray2 = BitArray([0, 0, 0, 1])

bitarray3 = bitarray1 | bitarray2
bitarray4 = bitarray1 & bitarray2
bitarray5 = ~bitarray1

print(bitarray3, type(bitarray3))
print(bitarray4, type(bitarray4))
print(bitarray5, type(bitarray5))

















