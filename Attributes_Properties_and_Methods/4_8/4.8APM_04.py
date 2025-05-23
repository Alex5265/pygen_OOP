# Класс BirthInfo 🌶️
# Реализуйте класс BirthInfo, описывающий данные о дате рождения. При создании экземпляра класс должен принимать один аргумент:
#
# birth_date — дата рождения, представленная в одном из следующих вариантов:
# экземпляр класса date
# строка с датой в ISO формате
# список или кортеж из трех целых чисел: года, месяца и дня
# Если дата рождения является некорректной или представлена в каком-либо другом формате, должно быть возбуждено исключение TypeError с текстом:
#
# Аргумент переданного типа не поддерживается
# Экземпляр класса BirthInfo должен иметь один атрибут:
#
# birth_date — дата рождения в виде экземпляра класса date
# Класс BirthInfo должен иметь одно свойство:
#
# age — свойство, доступное только для чтения, возвращающее текущий возраст в годах, то есть количество полных лет, прошедших с даты рождения на сегодняшний день
# Примечание 1. Возраст в годах должен вычисляться так же, как и обычный возраст человека, то есть в день рождения его возраст увеличивается на один год.
#
# Приведенный ниже код:
#
# birthinfo = BirthInfo(date(2023, 2, 26))
#
# print(birthinfo.age)
# в 2024-02-25 должен выводить:0
# в 2024-02-26 должен выводить:1
# в 2025-02-25 должен выводить:1
#  в 2025-02-26 должен выводить:2
# from functools import  singledispatchmethod
# from datetime import date
#
#
from datetime import date
from functools import singledispatchmethod


class BirthInfo:
    @singledispatchmethod
    def __init__(self, birth_date):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @__init__.register
    def _from_date(self, birth_date: date):
        self.birth_date = birth_date

    @__init__.register
    def _from_str(self, birth_date: str):
        try:
            self.birth_date = date.fromisoformat(birth_date)
        except ValueError:
            raise TypeError('Аргумент переданного типа не поддерживается') from None

    @__init__.register
    def _from_iter(self, birth_date: list | tuple):
        try:
            self.birth_date = date(*birth_date)
        except (TypeError, ValueError):
            raise TypeError('Аргумент переданного типа не поддерживается') from None

    @property
    def age(self):
        age = date.today().year - self.birth_date.year - 1
        print((date.today().month, date.today().day), (self.birth_date.month, self.birth_date.day))
        age += (date.today().month, date.today().day) >= (self.birth_date.month, self.birth_date.day)
        return age

birth_dates = [
    [2020],
    (2020,),
    [2020, 1],
    [2020, 1, '1'],
    (2020, 1),
    (2020, 1, '1'),
    [2020, 1, 1, 1],
    (2020, 1, 1, 1),
    [2020, '1', '1'],
    [2020, '1', 1],
]

for birth_date in birth_dates:
    try:
        birthinfo = BirthInfo(birth_date)
    except TypeError as e:
        print(e)


birthinfo1 = BirthInfo('2020-05-16')
birthinfo2 = BirthInfo(date(2010, 5, 18))
birthinfo3 = BirthInfo([2016, 5, 20])

print(birthinfo1.birth_date)
print(birthinfo2.birth_date)
print(birthinfo3.birth_date)

print(birthinfo1.age)
print(birthinfo2.age)
print(birthinfo3.age)







