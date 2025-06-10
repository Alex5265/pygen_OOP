# Класс SkipIterator
# Реализуйте класс SkipIterator. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# n — целое неотрицательное число
# Экземпляр класса SkipIterator должен являться итератором, который генерирует элементы итерируемого объекта iterable, пропуская по n элементов, а затем возбуждает исключение StopIteration.
#
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Класс SkipIterator должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.


class SkipIterator:
    def __init__(self, iterable, n):
        self.iterator = iter(iterable)
        self.n = n

    def __iter__(self):
        return self

    def __next__(self):
        el = next(self.iterator)

        for _ in range(self.n):
            next(self.iterator, None)

        return el



skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)   # пропускаем по одному элементу

print(*skipiterator)
print()

skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2)   # пропускаем по два элемента

print(*skipiterator)
print()

skipiterator = SkipIterator([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)   # не пропускаем элементы

print(*skipiterator)
print()

skipiterator = SkipIterator(iter([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 5)

print(*skipiterator)
















