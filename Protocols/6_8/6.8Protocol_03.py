# Класс LimitedTakes
# Реализуйте класс LimitedTakes, описывающий дескриптор, который позволяет получать значение атрибута лишь определенное количество раз. При создании экземпляра класс должен принимать один аргумент:
#
# times — количество доступных обращений к атрибуту
# Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.
#
# При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:
#
# Атрибут не найден
# Если к атрибуту было выполнено times обращений, во время всех последующих обращений должно возбуждаться исключение MaxCallsException с текстом:
#
# Превышено количество доступных обращений
# При установке или изменении значения атрибута дескриптор должен устанавливать или изменять это значение без каких-либо дополнительных проверок.
#
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализации класса LimitedTakes нет, она может быть произвольной.

class MaxCallsException(Exception):
    pass


class LimitedTakes:
    def __init__(self, times):
        self._times = times

    def __set_name__(self, cls, attr):
        self._attr = attr

    def __get__(self, obj, cls):
        if obj is None:
            return self
        if self._times:
            if self._attr in obj.__dict__:
                self._times -= 1
                return obj.__dict__[self._attr]
            raise AttributeError('Атрибут не найден')
        raise MaxCallsException('Превышено количество доступных обращений')

    def __set__(self, obj, value):
        obj.__dict__[self._attr] = value



class Student:
    name = LimitedTakes(3)

student = Student()
student.name = 'Gwen'

print(student.name)
print(student.name)
print(student.name)

try:
    print(student.name)
except MaxCallsException as e:
    print(e)

print()


class Student:
    name = LimitedTakes(3)


student = Student()

for _ in range(100):
    student.name = 'Gwen'

print(student.name)










