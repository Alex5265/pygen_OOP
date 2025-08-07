# Классы Weekday и NextDate
# 1. Реализуйте класс Weekday, описывающий перечисление с днями недели. Перечисление должно иметь семь элементов:
#
# MONDAY — элемент со значением 0
# TUESDAY — элемент со значением 1
# WEDNESDAY — элемент со значением 2
# THURSDAY — элемент со значением 3
# FRIDAY — элемент со значением 4
# SATURDAY — элемент со значением 5
# SUNDAY — элемент со значением 6
# 2. Также реализуйте класс NextDate, который позволяет определять следующую ближайшую дату, соответствующую указанному дню недели: например, дату ближайшего вторника или дату ближайшей пятницы. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#
# today — текущая дата, представленная экземпляром класса date. Относительно этой даты должна определяться следующая ближайшая дата, соответствующая некоторому дню недели
# weekday — день недели, представленный элементом перечисления Weekday
# considering_today — булево значение, по умолчанию равняется False
# Параметр considering_today должен определять, учитывается ли дата today при определении даты, соответствующей дню недели weekday. Если параметр имеет значение True, дата today должна учитываться, если False — не учитываться. Например, если день недели даты today равен weekday и параметр considering_today равен True, то искомой датой, соответствующей дню недели weekday, будет являться сама дата today.
#
# Класс NextDate должен иметь два метода экземпляра:
#
# date() — метод, возвращающий следующую ближайшую (относительно даты today) дату, соответствующую дню недели weekday, в виде экземпляра класса date
# days_until() — метод, возвращающий количество дней до следующей ближайшей (относительно даты today) даты, соответствующей дню недели weekday
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

from datetime import timedelta
from enum import IntEnum

Weekday = IntEnum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'], start=0)


class NextDate:
    def __init__(self, today, weekday, after_today=False):
        self.today = today
        self.weekday = weekday
        self.after_today = after_today

    def date(self):
        next_date = self.today + timedelta((self.weekday - self.today.weekday()) % 7)
        if not self.after_today and next_date == self.today:
            next_date += timedelta(7)
        return next_date

    def days_until(self):
        return (self.date() - self.today).days



from datetime import date

today = date(2023, 4, 17)                              # понедельник
next_friday = NextDate(today, Weekday.FRIDAY)          # следующая пятница

print(next_friday.date())
print(next_friday.days_until())
print()


from datetime import date

today = date(2023, 4, 17)                              # понедельник
next_monday = NextDate(today, Weekday.MONDAY)          # следующий понедельник без учета текущего

print(next_monday.date())
print(next_monday.days_until())
print()

from datetime import date

today = date(2023, 4, 17)                              # понедельник
next_monday = NextDate(today, Weekday.MONDAY, True)    # следующий понедельник с учетом текущего

print(next_monday.date())
print(next_monday.days_until())







