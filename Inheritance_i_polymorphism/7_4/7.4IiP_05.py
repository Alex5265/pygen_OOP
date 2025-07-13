# Класс NumberList
# Реализуйте класс NumberList, наследника класса UserList, описывающий список, элементами которого могут быть лишь числа. При создании экземпляра класс должен принимать один аргумент:
#
# iterable — итерируемый объект, определяющий начальный набор элементов экземпляра класса NumberList. Если хотя бы один элемент переданного итерируемого объекта не является числом, должно быть возбуждено исключение TypeError с текстом:
# Элементами экземпляра класса NumberList должны быть числа
# Итерируемый объект может быть не передан, в таком случае начальный набор элементов считается пустым
# При изменении экземпляра класса NumberList с помощью индексов, операций сложения (+, +=) и методов append(), extend() и insert() должна производиться проверка на то, что добавляемые элементы являются числами, в противном случае должно возбуждаться исключение TypeError с текстом:
#
# Элементами экземпляра класса NumberList должны быть числа
# Примечание 1. Числами будем считать экземпляры классов int и float.
#
# Примечание 2. Экземпляры класса NumberList должны поддерживать операции сложения (+, +=) и метод extend() как между собой, так и между любыми итерируемыми объектами.
#
# Примечание 3. Экземпляр класса NumberList не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса NumberList измениться  не должен.
#
# Примечание 4. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 5. Никаких ограничений касательно реализации класса NumberList нет, она может быть произвольной.
from collections import UserList

class NumberList(UserList):
    def __init__(self, iterable):
        super().__init__(self._check(item) for item in iterable)

    @staticmethod
    def _check(item):
        if isinstance(item, (int, float)):
            return item
        raise TypeError('Элементами экземпляра класса NumberList должны быть числа')

    def __setitem__(self, key, value):
        self._check(self.data[key])
        self.data[key] = self._check(value)

    def insert(self, i, item):
        self._check(item)
        return super().insert(i, item)

    def append(self, item):
        self._check(item)
        return super().append(item)

    def extend(self, other):
        for elem in other:
            self._check(elem)
        return super().extend(other)

    def __iadd__(self, other):
        for elem in other:
            self._check(elem)
        return super().__iadd__(other)


numberlist = NumberList([1, 2])

numberlist.append(3)
numberlist.extend([4, 5])
numberlist.insert(0, 0)
print(numberlist)
print()


numberlist = NumberList([0, 1.0])

numberlist[1] = 1
numberlist = numberlist + NumberList([2, 3])
numberlist += NumberList([4, 5])
print(numberlist)
print()


try:
    numberlist = NumberList(['a', 'b', 'c'])
except TypeError as error:
    print(error)
print()


numberlist = NumberList([1, 2, 3])

try:
    numberlist.append('4')
except TypeError as error:
    print(error)












