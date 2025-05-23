# Класс Version
# Реализуйте класс Version, описывающий версию программного обеспечения. При создании экземпляра класс должен принимать один аргумент:
#
# version — строка из трех целых чисел, разделенных точками и описывающих версию ПО. Например, 2.8.1. Если одно из чисел не указано, оно считается равным нулю. Например, версия 2 равнозначна версии 2.0.0, а версия 2.8 равнозначна версии 2.8.0
# Экземпляр класса Version должен иметь следующее формальное строковое представление:
#
# Version('<версия ПО в виде трех целых чисел, разделенных точками>')
# И следующее неформальное строковое представление:
#
# <версия ПО в виде трех целых чисел, разделенных точками>
# Также экземпляры класса Version должны поддерживать между собой все операции сравнения с помощью операторов ==, !=, >, <, >=, <=. Два Version объекта считаются равными, если все три числа в их версиях совпадают. Version объект считается больше другогоVersion объекта, если первое число в его версии больше. Или если второе число в его версии больше, если первые числа совпадают. Или если третье число в его версии больше, если первые и вторые числа совпадают.
#
# Примечание 1. Если объект, с которым выполняется операция сравнения, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
#
# Примечание 2. Никаких ограничений касательно реализации класса Version нет, она может быть произвольной.
from functools import singledispatchmethod, total_ordering

@total_ordering
class Version:
    def __init__(self, version):
        res = version.split('.')
        if len(res) == 1:
            self.version = f'{version.strip()}.{0}.{0}'
        elif len(res) == 2:
            self.version = f'{version}.{0}'
        elif len(res) == 3:
            self.version = version

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.version}')"

    def __str__(self):
        return self.version

    def __eq__(self, other):
        if isinstance(other, Version):
            return tuple(map(int, self.version.split('.'))) == tuple(map(int, other.version.split('.')))
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Version):
            return tuple(map(int, self.version.split('.'))) < tuple(map(int, other.version.split('.')))
        return NotImplemented


print(Version('3.0.3') == Version('1.11.28'))
print(Version('3.0.3') < Version('1.11.28'))
print(Version('3.0.3') > Version('1.11.28'))
print(Version('3.0.3') <= Version('1.11.28'))
print(Version('3.0.3') >= Version('1.11.28'))

versions = [Version('2'), Version('2.1'), Version('1.9.1')]

print(sorted(versions))
print(min(versions))
print(max(versions))






