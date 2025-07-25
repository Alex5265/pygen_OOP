# Класс NonKeyword
# Реализуйте класс NonKeyword, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение атрибута не является строковым ключевым словом в Python. При создании экземпляра класс должен принимать один аргумент:
#
# name — имя атрибута, за которым будет закреплен дескриптор
# При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:
#
# Атрибут не найден
# При установке или изменении значения атрибута дескриптор должен проверять, не является ли это значение строковым ключевым словом в Python. Если значение является строковым ключевым словом, должно быть возбуждено исключение ValueError с текстом:
#
# Некорректное значение
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализации класса NonKeyword нет, она может быть произвольной.
from keyword import kwlist

class NonKeyword:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.name in instance.__dict__:
            return instance.__dict__[self.name]
        else:
            raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        if value in kwlist:
            raise ValueError('Некорректное значение')
        instance.__dict__[self.name] = value





class Student:
    name = NonKeyword('name')

student = Student()
student.name = 'Peter'

print(student.name)

print()

class Student:
    name = NonKeyword('name')

student = Student()

try:
    print(student.name)
except AttributeError as e:
    print(e)

print()


class Student:
    name = NonKeyword('name')

student = Student()
student.name = 'Peter'

try:
    student.name = 'class'
except ValueError as e:
    print(e)

class NonKeywordData:
    obj = NonKeyword('obj')


data = [1, 2.3, [4, 5, 6], (7, 8, 9), {10: 11, 12: 13, 14: 15}, True, False, 'Mantrida']
nonkeyworddata = NonKeywordData()

for item in data:
    nonkeyworddata.obj = item
    print(nonkeyworddata.obj)

class Student:
    name = NonKeyword('name')

print(Student.name.__class__)






