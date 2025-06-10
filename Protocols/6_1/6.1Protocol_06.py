# Класс Peekable 🌶️
# Реализуйте класс Peekable. При создании экземпляра класс должен принимать один аргумент:
#
# iterable — итерируемый объект
# Экземпляр класса Peekable должен являться итератором, который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.
#
# Класс Peekable должен иметь один метод экземпляра:
#
# peek() — метод, возвращающий следующий элемент итератора аналогично функции next(), но при этом не сдвигающий итератор. Если итератор пуст, должно быть возбуждено исключение StopIteration. Также метод должен уметь принимать один необязательный аргумент default — объект, который будет возвращен вместо возбуждения исключения StopIteration, если итератор пуст
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Класс Peekable должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.


ETERNITY = object()

class Peekable:
    def __init__(self, iterable):
        self.it = iter(iterable)
        self.cache = []

    def __iter__(self):
        return self

    def __next__(self):
        self.peek()
        return self.cache.pop()

    def peek(self, default=ETERNITY):
        if not self.cache:
            try:
                self.cache.append(next(self.it))
            except StopIteration:
                if default is not ETERNITY:
                    return default
                raise
        return self.cache[0]



iterator = Peekable('beegeek')

print(next(iterator))
print(next(iterator))
print(*iterator)
print()

iterator = Peekable('Python')

print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print(next(iterator))
print(iterator.peek())
print(iterator.peek())
print()

iterator = Peekable('Python')

print(*iterator)
print(iterator.peek(None))

iterator = Peekable(iter([]))

try:
    iterator.peek()
except StopIteration:
    print('Пустой итератор')

try:
    next(iterator)
except StopIteration:
    print('Пустой итератор')


iterator = Peekable([n ** 2 for n in [1, 2, 3]])

print(iterator.peek(default=0))
print(*iterator)
print(iterator.peek(default=None))
print(iterator.peek(default=1))
print(iterator.peek(default=[]))
print(iterator.peek(default=()))

