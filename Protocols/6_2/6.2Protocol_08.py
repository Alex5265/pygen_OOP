# Класс Grouper🌶️
# Нередко нам приходится группировать объекты по определенному признаку. Например, строки можно сгруппировать по их длине или первому символу. Реализуйте класс Grouper, описывающий объект, который группирует элементы некоторого итерируемого объекта на основе ключевой функции. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# key — ключевая функция
# Элементы попадают в одну группу, если при их передаче в ключевую функцию она возвращает один и тот же результат.  Например, elem1 и elem2 попадают в одну группу, если key(elem1) == key(elem2). Значение key(elem1) будем называть ключом группы, а elem1 и elem2 — элементами группы по этому ключу.
#
# Класс Grouper должен иметь два метода экземпляра:
#
# add() — метод, принимающий в качестве аргумента произвольный объект и добавляющий его в нужную группу экземпляра класса Grouper
# group_for() — метод, принимающий в качестве аргумента произвольный объект, определяющий, в какую группу экземпляра класса Grouper попадет этот объект, и возвращающий ключ этой группы
# При передаче экземпляра класса Grouper в функцию len() должно возвращаться количество групп в нем.
#
# Помимо этого, экземпляр класса Grouper должен быть итерируемым объектом, то есть позволять перебирать свои группы, например, с помощью цикла for. В данном случае группа — это кортеж, первым элементом которого является ключ группы, вторым — список элементов группы. Группы при итерировании могут располагаться в произвольном порядке.
#
# Также экземпляр класса Grouper должен поддерживать операцию проверки на принадлежность с помощью оператора in, в которой проверяется наличие в экземпляре класса Grouper группы с искомым ключом.
#
# Наконец, экземпляр класса Grouper должен позволять получать элементы группы по ключу. В данном случае элементы группы должны быть представлены в виде списка, при этом элементы в списке должны располагаться в том порядке, в котором они были добавлены.
#
# Примечание 1. Экземпляр класса Grouper не должен зависеть от итерируемого объекта, на основе которого он был создан. Другими словами, если исходный итерируемый объект изменится, то экземпляр класса Grouper измениться  не должен.
#
# Примечание 2. Реализация класса Grouper может быть произвольной, то есть требований к наличию определенных атрибутов нет.
#
# Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.


class Grouper:
    def __init__(self, iterable, key):
        self.key = key
        self._make_group(iterable)

    def _make_group(self, iterable):
        self._dict = {}
        for el in iterable:
            self.add(el)

    def add(self, value):
        self._dict.setdefault(self.key(value), []).append(value)

    def group_for(self, value):
        return self.key(value)

    def __len__(self) -> int:
        return len(self._dict)

    def __iter__(self):
        yield from self._dict.items()

    def __contains__(self, item) -> bool:
        return item in self._dict

    def __getitem__(self, key):
        return self._dict[key]


# grouper = Grouper(['bee', 'geek', 'one', 'two', 'five', 'hi'], key=len)
#
# print(grouper[2])
# print(grouper[3])
# print(grouper[4])
# print(*grouper)

grouper = Grouper(['hi'], key=lambda s: s[0])
print(len(grouper))

grouper.add('hello')
grouper.add('bee')
grouper.add('big')

print(len(grouper))

grouper.add('geek')
print(grouper['h'])
print(grouper['b'])
print(grouper['g'])

print(*grouper)




