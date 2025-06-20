# Класс TypeChecked
# Реализуйте класс TypeChecked, описывающий дескриптор, который проверяет, что устанавливаемое или изменяемое значение атрибута принадлежит определенному типу данных. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых является типом данных.
#
# Дескриптор должен закрепляться за атрибутом, имеющим то же имя, что и переменная, которой присваивается дескриптор.
#
# При обращении к атрибуту дескриптор должен возвращать значение этого атрибута, если оно установлено. Если значение атрибута не установлено, должно быть возбуждено исключение AttributeError с текстом:
#
# Атрибут не найден
# При установке или изменении значения атрибута дескриптор должен проверять, принадлежит ли это значение одному из типов, указанных при создании дескриптора. Если значение не принадлежит ни одному из типов, должно быть возбуждено исключение TypeError с текстом:
#
# Некорректное значение
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализации класса TypeChecked нет, она может быть произвольной.

class TypeChecked:
    def __init__(self, *args):
        self.tupes = args

    def __set_name__(self, owner, name):
        self.attr = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        if self.attr in instance.__dict__:
            return instance.__dict__[self.attr]
        raise AttributeError('Атрибут не найден')

    def __set__(self, instance, value):
        if not isinstance(value, self.tupes):
            raise TypeError('Некорректное значение')
        instance.__dict__[self.attr] = value


class Student:
    name = TypeChecked(str)

student = Student()
student.name = 'Mary'

print(student.name)

print()


class Student:
    name = TypeChecked(str)

student = Student()
student.name = 'Mary'

try:
    student.name = 99
except TypeError as e:
    print(e)

print(student.name)

print()


class Student:
    age = TypeChecked(int, float)

student = Student()

student.age = 18
print(student.age)

student.age = 18.5
print(student.age)











