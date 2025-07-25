# Класс Queue 🌶️
# Очередь — абстрактный тип данных с дисциплиной доступа к элементам "первый пришёл — первый вышел". Добавление элемента возможно лишь в конец очереди, выборка — только из начала очереди, при этом выбранный элемент из очереди удаляется.
#
# Реализуйте класс Queue, описывающий очередь. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является элементом очереди. Порядок следования аргументов образует порядок элементов в очереди, то есть первый аргумент — первый элемент очереди, второй аргумент — второй элемент очереди, и так далее.
#
# Класс Queue должен иметь два метода экземпляра:
#
# add() — метод, принимающий произвольное количество позиционных аргументов и добавляющий их в конец очереди в том порядке, в котором они были переданы
# pop() — метод, удаляющий из очереди первый элемент и возвращающий его. Если очередь пуста, метод должен вернуть значение None
# Экземпляр класса Queue должен иметь следующее неформальное строковое представление:
#
# <первый элемент очереди> -> <второй элемент очереди> -> <третий элемент очереди> -> ...
# Помимо этого, экземпляры класса Queue должны поддерживать между собой операции сравнения с помощью операторов == и!=. Две очереди считаются равными, если они имеют равную длину и содержат равные элементы на равных позициях.
#
# Также экземпляры класса Queue должны поддерживать между собой операцию сложения с помощью операторов + и +=:
#
# результатом сложения с помощью оператора + должен являться новый экземпляр класса Queue, представляющий очередь со всеми элементами исходных очередей: сначала все элементы левой очереди, затем все элементы правой очереди
# результатом сложения с помощью оператора += должен являться левый экземпляр класса Queue, представляющий очередь, к которой добавлены все элементы правой очереди
# Наконец, экземпляр класса Queue должен поддерживать операцию побитового сдвига вправо на целое число n с помощью оператора >>, результатом которой должен являться новый экземпляр класса Queue, представляющий исходную очередь без первых n элементов. Если n больше или равно длине исходной очереди, результатом должен являться экземпляр класса Queue, представляющий пустую очередь.
#
# Примечание 1. Если объект, с которым выполняется операция сравнения или арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
#
# Примечание 2. Никаких ограничений касательно реализации класса Queue нет, она может быть произвольной.

class Queue:
    def __init__(self, *args):
        self.val = list(args)

    def add(self, *args):
        self.val.extend(args)

    def pop(self):
        if self.val:
            return self.val.pop(0)
        return None

    def __str__(self):
        return ' -> '.join(map(str, self.val))

    def __eq__(self, other):
        if isinstance(other, Queue):
            return self.val == other.val
        return NotImplemented

    def __add__(self, other):
        if isinstance(other, Queue):
            return Queue(*(self.val + other.val))
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Queue):
            self.add(other)
            return self
        return NotImplemented

    def __rshift__(self, other):
        if isinstance(other, int):
            return Queue(*self.val[other:])
        return NotImplemented


queue = Queue(1, 2)
queue.add(3)
queue.add(4, 5)

print(queue)
print(queue.pop())
print(queue)
print()


queue1 = Queue(1, 2, 3)
queue2 = Queue(1, 2)

print(queue1 == queue2)
queue2.add(3)
print(queue1 == queue2)
print()


queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

print(queue1 + queue2)
print()

queue1 = Queue(1, 2, 3)
queue2 = Queue(4, 5)

queue1 += queue2

print(queue1)

print()

queue = Queue(1, 2, 3, 4, 5)

print(queue >> 3)







