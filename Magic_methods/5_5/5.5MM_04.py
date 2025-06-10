# Класс Time
# Реализуйте класс Time, описывающий время на цифровых часах. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
#
# hours — количество часов; каждые 24 часа должны преобразовываться в 0 часов
# minutes — количество минут; каждые 60 минут должны преобразовываться в 1 час
# Экземпляр класса Time должен иметь следующее неформальное строковое представление:
#
# <количество часов в формате HH>:<количество минут в формате MM>
# Также экземпляры класса Time должны поддерживать между собой операцию сложения с помощью операторов + и +=:
#
# результатом сложения с помощью оператора + должен являться новый экземпляр класса Time, количество часов которого равно сумме часов исходных экземпляров класса Time, количество минут — сумме минут исходных экземпляров класса Time
# результатом сложения с помощью оператора += должен являться левый экземпляр класса Time, количество часов которого увеличено на количество часов правого экземпляра класса Time, количество минут — на количество минут правого экземпляра класса Time
# Примечание 1. Если объект, с которым выполняется арифметическая операция, некорректен, метод, реализующий эту операцию, должен вернуть константу NotImplemented.
#
# Примечание 2. Никаких ограничений касательно реализации класса Time нет, она может быть произвольной.


class Time:
    def __init__(self, hours, minutes):
        self.hours, self.minutes = self._normalize(hours, minutes)

    @staticmethod
    def _normalize(hours, minutes):
        return (hours + minutes // 60) % 24, minutes % 60

    def __str__(self):
        return f'{self.hours:>02}:{self.minutes:>02}'

    def __add__(self, other):
        if isinstance(other, Time):
            return Time(self.hours + other.hours, self.minutes + other.minutes)
        return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Time):
            self.hours, self.minutes = self._normalize(self.hours + other.hours, self.minutes + other.minutes)
            return self
        return NotImplemented




time1 = Time(2, 30)
time2 = Time(3, 10)

print(time1 + time2)
print(time2 + time1)
print()


time1 = Time(2, 30)
time2 = Time(3, 10)

time1 += time2

print(time1)
print(time2)
print()

time1 = Time(25, 20)
time2 = Time(10, 130)

print(time1)
print(time2)
print()

t = Time(22, 0)
t += Time(3, 0)
print(t)

