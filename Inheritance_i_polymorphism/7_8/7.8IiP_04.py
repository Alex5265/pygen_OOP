# Класс Queue
# Реализуйте класс Queue, описывающий очередь, элементами которой являются пары ключ: значение. При создании экземпляра класс должен принимать один аргумент:
#
# pairs — список или словарь, определяющий начальный набор элементов очереди. Порядок элементов в очереди должен совпадать с их порядком в переданном итерируемом объекте. Если не передан, очередь считается пустой
# Класс Queue должен иметь два метода экземпляра:
#
# add() — метод, принимающий в качестве аргумента элемент и добавляющий его в конец очереди. Элементом в данном случае является двухэлементный кортеж, содержащий ключ и значение. Если в очереди уже содержится элемент с указанным ключом, он должен быть перенесен в конец очереди, а его значение должно быть обновлено
# pop() — метод, удаляющий из очереди первый элемент и возвращающий его. Элементом в данном случае является двухэлементный кортеж, содержащий ключ и значение. Если очередь пуста, должно быть возбуждено исключение KeyError с текстом:
# Очередь пуста
# Экземпляр класса Queue должен иметь следующее формальное строковое представление:
#
# Queue([(<ключ 1-го элемента>, <значение 1-го элемента>), (<ключ 2-го элемента>, <значение 2-го элемента>), ...])
# При передаче экземпляра класса Queue в функцию len() должно возвращаться количество элементов в нем.
#
# Примечание 1. Вероятно, при решении задачи будет удобно воспользоваться одним из классов из модуля collections.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 3. Никаких ограничений касательно реализации класса Queue нет, она может быть произвольной.

from collections import OrderedDict


class Queue:
    def __init__(self, initial_data=None):
        self.data = OrderedDict()
        if initial_data is not None:
            self.data.update(initial_data)

    def add(self, item):
        key, value = item
        if key in self.data:
            self.data.move_to_end(key)
        self.data[key] = value

    def pop(self):
        try:
            return self.data.popitem(last=False)
        except KeyError as e:
            e.args = ('Очередь пуста',)
            raise

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return f'Queue({list(self.data.items())})'



queue = Queue()

queue.add(('one', 1))
queue.add(('two', 2))
print(queue)
print()

queue = Queue([('one', 1)])

queue.add(('two', 2))
print(queue.pop())
print(queue.pop())
print(queue)
print()


queue = Queue({'one': 1, 'two': 2})

print(len(queue))
queue.add(('three', 1))
print(len(queue))
print()


queue = Queue()

queue.add(('one', 1))
queue.add(('two', 2))
print(queue)
queue.add(('one', 10))
print(queue)
print()

queue = Queue()

try:
    queue.pop()
except KeyError as error:
    print(error)



