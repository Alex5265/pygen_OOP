# Класс OrderedSet
# Реализуйте класс OrderedSet, описывающий упорядоченное множество. При создании экземпляра класс должен принимать один аргумент:
#
# iterable — итерируемый объект, определяющий начальный набор элементов упорядоченного множества. Если не передан, начальный набор элементов считается пустым
# Класс OrderedSet должен иметь два метода экземпляра:
#
# add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в конец упорядоченного множества
# discard() — метод, принимающий в качестве аргумента произвольный объект и удаляющий его из упорядоченного множества, если он в нем присутствует
# При передаче экземпляра класса OrderedSet в функцию len() должно возвращаться количество элементов в нем.
#
# Помимо этого, экземпляр класса OrderedSet должен быть итерируемым объектом, то есть позволять перебирать свои элементы, например, с помощью цикла for.
#
# Также экземпляр класса OrderedSet должен поддерживать операцию проверки на принадлежность с помощью оператора in.
#
# Наконец, экземпляры класса OrderedSet должны поддерживать операции сравнения с помощью операторов == и !=. Методы, реализующие операции сравнения, должны уметь сравнивать как два экземпляра класса OrderedSet между собой, так и экземпляр класса OrderedSet с экземпляром класса set. Если упорядоченное множество сравнивается с упорядоченным множеством, они считаются равными в том случае, если они имеют равную длину и содержат равные элементы на равных позициях. Если упорядоченное множество сравнивается с обычным множеством, они считаются равными в том случае, если имеют равную длину и содержат равные элементы без учета их расположения.
#
# Примечание 1. Экземпляр класса OrderedSet не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса OrderedSet измениться  не должен.
#
# Примечание 2. Если объект, с которыми происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.
#
# Примечание 3. Никаких ограничений касательно реализации класса OrderedSet нет, она может быть произвольной.


class OrderedSet:
    def __init__(self, iterable=()):
        self.it = dict.fromkeys(iterable, None)

    def __len__(self):
        return len(self.it)

    def __iter__(self):
        yield from self.it.keys()

    def __contains__(self, item):
        return item in self.it

    def __eq__(self, other):
        if isinstance(other, OrderedSet):
            return tuple(self.it.keys()) == tuple(other.it.keys())
        elif isinstance(other, set):
            return set(self.it.keys()) == other
        return NotImplemented

    def add(self, item):
        self.it.setdefault(item, None)

    def discard(self, item):
        self.it.pop(item, None)


orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print(*orderedset)
print(len(orderedset))
print()

orderedset = OrderedSet(['bee', 'python', 'stepik', 'bee', 'geek', 'python', 'bee'])

print('python' in orderedset)
print('C++' in orderedset)
print()


orderedset = OrderedSet()

orderedset.add('green')
orderedset.add('green')
orderedset.add('blue')
orderedset.add('red')
print(*orderedset)
orderedset.discard('blue')
orderedset.discard('white')
print(*orderedset)

print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['green', 'red', 'blue']))
print(OrderedSet(['green', 'red', 'blue']) == OrderedSet(['red', 'blue', 'green']))
print(OrderedSet(['green', 'red', 'blue']) == {'blue', 'red', 'green'})
print(OrderedSet(['green', 'red', 'blue']) == ['green', 'red', 'blue'])
print(OrderedSet(['green', 'red', 'blue']) == 100)


data = ['Ada Lovelace'] * 1000
orderedset = OrderedSet(data)

print(len(orderedset))

orderedset = OrderedSet([1, 2, 3, 4])
not_supported = [120, {1: 'one'}, True, 'pi = 3', 17.9]

for item in not_supported:
    print(item != orderedset)


orderedset = OrderedSet([1, 2, 3, 4])
print(orderedset.__eq__(1))
print(orderedset.__ne__(1.1))


