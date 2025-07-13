# Классы Lecture и Conference🌶️🌶️
# 1. Реализуйте класс Lecture, описывающий некоторое выступление. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#
# topic — тема выступления
# start_time — время начала выступления в виде строки в формате HH:MM
# duration — длительность выступления в виде строки в формате HH:MM
# 2. Также реализуйте класс Conference, описывающий конференцию, протяженностью в один день. Конференция представляет собой набор последовательных выступлений. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Класс Conference должен иметь четыре метода экземпляра:
#
# add() — метод, принимающий в качестве аргумента выступление и добавляющий его в конференцию. Если выступление пересекается по времени с другими выступлениями, должно быть возбуждено исключение ValueError с текстом:
# Провести выступление в это время невозможно
# total() — метод, возвращающий суммарную длительность всех выступлений в конференции в виде строки в формате HH:MM
# longest_lecture() — метод, возвращающий длительность самого долгого выступления в конференции в виде строки в формате HH:MM
# longest_break() — метод, возвращающий длительность самого долгого перерыва между выступлениями в конференции в виде строки в формате HH:MM
# Примечание 1. Перерыв между выступлениями может быть нулевым. Другими словами, одно выступление может заканчиваться, например, в 12:00, а другое начинаться в 12:00.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованные классы используются только с корректными данными.
#
# Примечание 3. Никаких ограничений касательно реализаций классов нет, они могут быть произвольными.

from bisect import insort
from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta


class Lecture:
    _PATTERN = '%H:%M'

    def __init__(self, topic, start_time, duration):
        self.topic = topic
        self.start_time = datetime.strptime(start_time, self._PATTERN)
        self.duration = datetime.strptime(duration, self._PATTERN)
        self.end_time = self.start_time + timedelta(hours=self.duration.hour, minutes=self.duration.minute)


class Conference:
    def __init__(self):
        self.lectures = []

    def add(self, lecture):
        for cur_lecture in self.lectures:
            if any((
                    cur_lecture.start_time <= lecture.start_time < cur_lecture.end_time,
                    lecture.start_time <= cur_lecture.start_time < lecture.end_time,
            )):
                raise ValueError('Провести выступление в это время невозможно')
        insort(self.lectures, lecture, key=lambda item: item.start_time)

    def total(self):
        total = sum((lecture.end_time - lecture.start_time for lecture in self.lectures), start=relativedelta())
        return f'{total.hours:0>2}:{total.minutes:0>2}'

    def longest_lecture(self):
        longest = max(lecture.duration for lecture in self.lectures)
        return f'{longest.hour:0>2}:{longest.minute:0>2}'

    def longest_break(self):
        longest = max(self.lectures[i + 1].start_time - self.lectures[i].end_time for i in range(len(self.lectures) - 1))
        hours, minutes = int(longest.total_seconds()) // 3600, (int(longest.total_seconds()) // 60) % 60
        return f'{hours:0>2}:{minutes:0>2}'



conference = Conference()

conference.add(Lecture('Простые числа', '08:00', '01:30'))
conference.add(Lecture('Жизнь после ChatGPT', '10:00', '02:00'))
conference.add(Lecture('Муравьиный алгоритм', '13:30', '01:50'))
print(conference.total())
print(conference.longest_lecture())
print(conference.longest_break())
print()

conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:30'))

try:
    conference.add(Lecture('Жизнь после ChatGPT', '09:00', '02:00'))
except ValueError as error:
    print(error)

print()

conference = Conference()
conference.add(Lecture('Простые числа', '08:00', '01:00'))
conference.add(Lecture('Жизнь после ChatGPT', '11:00', '02:00'))

try:
    conference.add(Lecture('Муравьиный алгоритм', '10:00', '04:00'))
except ValueError as error:
    print(error)




















