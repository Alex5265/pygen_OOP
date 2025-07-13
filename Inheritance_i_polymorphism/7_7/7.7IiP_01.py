# Классы USADate и ItalianDate
# 1. Реализуйте класс USADate, описывающий дату в американском формате. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#
# year — год
# month — месяц
# day — день
# Класс USADate должен иметь два метода экземпляра:
#
# format() — метод, который возвращает строку, представляющую собой дату в формате MM-DD-YYYY
# iso_format() — метод, который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
# 2. Также реализуйте класс ItalianDate, описывающий дату в итальянском формате, конструктор которого принимает три аргумента:
#
# year — год
# month — месяц
# day — день
# Класс ItalianDate должен иметь два метода экземпляра:
#
# format() — метод, который возвращает строку, представляющую собой дату в формате DD/MM/YYYY
# iso_format() — метод, который возвращает строку, представляющую собой дату в формате YYYY-MM-DD
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.
from abc import ABC, abstractmethod

class CountyData(ABC):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @abstractmethod
    def format(self):
        pass

    def iso_format(self):
        return f'{self.year}-{self.month:02}-{self.day:02}'

class USADate(CountyData):
    def format(self):
        return f"{self.month:02}-{self.day:02}-{self.year}"

class ItalianDate(CountyData):
    def format(self):
        return f'{self.day:02}/{self.month:02}/{self.year}'


usadate = USADate(2023, 4, 6)

print(usadate.format())
print(usadate.iso_format())
print()


italiandate = ItalianDate(2023, 4, 6)

print(italiandate.format())
print(italiandate.iso_format())



# решение из курса


from abc import ABC, abstractmethod
from datetime import date


class DateFormat(ABC):
    def __init__(self, year, month, day):
        self._date = date(year, month, day)

    def iso_format(self):
        return self._date.isoformat()

    @abstractmethod
    def format(self):
        pass


class USADate(DateFormat):
    def format(self):
        return self._date.strftime('%m-%d-%Y')


class ItalianDate(DateFormat):
    def format(self):
        return self._date.strftime('%d/%m/%Y')








