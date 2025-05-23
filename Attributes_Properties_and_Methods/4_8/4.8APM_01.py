# Класс Processor
# Вам доступен класс Processor. При создании экземпляра класс не принимает никаких аргументов.
#
# Класс Processor имеет один статический метод:
#
# process() — метод, который принимает в качестве аргумента произвольный объект, преобразует его в зависимости от его типа и возвращает полученный результат. Если тип переданного объекта не поддерживается методом, возбуждается исключение TypeError с текстом:
# Аргумент переданного типа не поддерживается
# Перепишите метод process() класса Processor с использованием декоратора @singledispatchmethod, чтобы он выполнял ту же задачу.
#
# Примечание 1. Примеры преобразования объектов всех поддерживаемых типов показаны в методе process() класса Processor.
#
# Примечание 2. Никаких ограничений касательно реализации класса Processor нет, она может быть произвольной.

class Processor:
    @staticmethod
    def process(data):
        if isinstance(data, (int, float)):
            return data * 2
        elif isinstance(data, str):
            return data.upper()
        elif isinstance(data, list):
            return sorted(data)
        elif isinstance(data, tuple):
            return tuple(sorted(data))
        raise TypeError('Аргумент переданного типа не поддерживается')


# результат:

from functools import singledispatchmethod

class Processor:

    @singledispatchmethod
    @staticmethod
    def process(data):
        raise TypeError('Аргумент переданного типа не поддерживается')

    @process.register
    @staticmethod
    def _tuple_process(data: tuple):
        return tuple(sorted(data))

    @process.register
    @staticmethod
    def _list_process(data: list):
        return sorted(data)

    @process.register
    @staticmethod
    def _srt_process(data: str):
        return data.upper()

    @process.register
    @staticmethod
    def _int_float_process(data: int | float):
        return data * 2


print(Processor.process(10))
print(Processor.process(5.2))
print(Processor.process('hello'))
print(Processor.process((4, 3, 2, 1)))
print(Processor.process([3, 2, 1]))

try:
    Processor.process({1, 2, 3})
except TypeError as e:
    print(e)
