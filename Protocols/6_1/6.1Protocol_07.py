# Класс LoopTracker🌶️
# Реализуйте класс LoopTracker. При создании экземпляра класс должен принимать один аргумент:
#
# iterable — итерируемый объект
# Экземпляр класса LoopTracker должен являться итератором, который генерирует элементы итерируемого объекта iterable в исходном порядке, а затем возбуждает исключение StopIteration.
#
# Класс LoopTracker должен иметь четыре свойства:
#
# accesses — свойство, доступное только для чтения, возвращающее количество элементов, сгенерированных итератором на данный момент
# empty_accesses — свойство, доступное только для чтения, возвращающее количество попыток получить следующий элемент опустевшего итератора
# first — свойство, доступное только для чтения, возвращающее первый элемент итератора и не сдвигающее его. Если итератор не имеет первого элемента, то есть создан на основе пустого итерируемого объекта, то должно быть возбуждено исключение AttributeError с текстом:
# Исходный итерируемый объект пуст
# last — свойство, доступное только для чтения, возвращающее последний элемент, сгенерированный итератором на данный момент. Если итератор еще не сгенерировал ни одного элемента, то должно быть возбуждено исключение AttributeError с текстом:
# Последнего элемента нет
# Класс LoopTracker должен иметь один метод экземпляра:
#
# is_empty() — метод, возвращающий True, если итератор опустошен, или False в противном случае
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Класс LoopTracker должен удовлетворять протоколу итератора, то есть иметь методы __iter__() и __next__(). Реализация же протокола может быть произвольной.



class LoopTracker:
    def __init__(self, iterable):
        self.iterable = iter(iterable)
        self._first = self._next = next(self.iterable,None)
        self._accesses = 0
        self._empty_accesses = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._next is not None:
            self._accesses += 1
            self._last = result = self._next
            self._next = next(self.iterable,None)
            return result
        else:
            self._empty_accesses +=1
            raise StopIteration

    @property
    def accesses(self):
        return self._accesses

    @property
    def empty_accesses(self):
        return self._empty_accesses

    @property
    def first(self):
        if self._first is not None:
            return self._first
        else:
            raise AttributeError('Исходный итерируемый объект пуст')

    @property
    def last(self):
        try:
            return self._last
        except:
            raise AttributeError ('Последнего элемента нет')

    def is_empty(self):
        if self._next:
            return False
        return True





loop_tracker = LoopTracker([1, 2])

print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())
next(loop_tracker)
print(loop_tracker.is_empty())







