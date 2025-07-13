# Функция get_method_owner()
# Реализуйте функцию get_method_owner(), которая принимает два аргумента в следующем порядке:
#
# cls — произвольный класс
# method — строковое название метода
# Функция должна возвращать класс, от которого класс cls унаследовал метод method. Если метода method нет ни в самом классе, ни в одном другом классе из его иерархии, функция get_method_owner() должна вернуть значение None.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию get_method_owner(), но не код, вызывающий ее.


def get_method_owner(cls, obj):
    for i in cls.mro():
        if obj in i.__dict__:
            return i


class A:
    def m(self):
        pass


class B(A):
    pass


print(get_method_owner(B, 'm'))
print()


class A:
    def m(self):
        pass


class B(A):
    def m(self):
        pass


print(get_method_owner(B, 'm'))
print()

class A:
    pass


class B(A):
    pass


print(get_method_owner(B, 'm'))






