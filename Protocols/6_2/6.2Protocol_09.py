# Класс MutableString 🌶️🌶️
# Реализуйте класс MutableString, описывающий изменяемую строку. При создании экземпляра класс должен принимать один аргумент:
#
# string — строка, определяющая начальное значение изменяемой строки. Если не передана, строка считается пустой
# Класс MutableString должен иметь два метода экземпляра:
#
# lower() — метод, переводящий все символы изменяемой строки в нижний регистр
# upper() — метод, переводящий все символы изменяемой строки в верхний регистр
# Экземпляр класса MutableString должен иметь неформальное строковое представление в следующем виде:
#
# <текущее значение изменяемой строки>
# Также экземпляр класса MutableString должен иметь формальное строковое представление в следующем виде:
#
# MutableString('<текущее значение изменяемой строки>')
# При передаче экземпляра класса MutableString в функцию len() должно возвращаться количество символов в нем.
#
# Помимо этого, экземпляр класса MutableString должен быть итерируемым объектом, то есть позволять перебирать свои символы, например, с помощью цикла for.
#
# Также экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных. Экземпляр класса MutableString должен поддерживать полноценные срезы. Результатом индексации и срезов должны быть новые изменяемые строки.
#
# Наконец, экземпляры класса MutableString должны поддерживать между собой операцию сложения с помощью оператора +, результатом которой должен являться новый экземпляр класса MutableString, представляющий конкатенацию исходных.
#
# Примечание 1. Реализация класса MutableString может быть произвольной, то есть требований к наличию определенных атрибутов нет.
#
# Примечание 2. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.


class MutableString:
    def __init__(self, string=''):
        self.string = string

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.string}')"

    def __str__(self):
        return self.string

    def __iter__(self):
        yield from self.string

    def __len__(self):
        return len(self.string)

    def __getitem__(self, item):
        return MutableString(self.string[item])

    def __setitem__(self, key, value):
        string = list(self.string)
        string[key] = value
        self.string = ''.join(string)

    def __delitem__(self, key):
        string = list(self.string)
        del string[key]
        self.string = ''.join(string)

    def __add__(self, other):
        if isinstance(other, MutableString):
            return MutableString(self.string + other.string)
        return NotImplemented

    def lower(self):
        self.string = self.string.lower()

    def upper(self):
        self.string = self.string.upper()






mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)








