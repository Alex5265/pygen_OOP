# Декоратор @takes_numbers
# Реализуйте класс декоратор @takes_numbers, который проверяет, что все аргументы, передаваемые в декорируемую функцию, принадлежат типам int или float. Если хотя бы один аргумент принадлежит какому-либо другому типу, должно быть возбуждено исключение TypeError с текстом:
#
# Аргументы должны принадлежать типам int или float
# Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @takes_numbers, но не код, вызывающий его.
import functools

class takes_numbers:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    @staticmethod
    def check_args(val):
        if isinstance(val, tuple):
            return all(isinstance(i, (int,float)) for i in val)
        elif isinstance(val, dict):
            return all(isinstance(val[i], (int,float)) for i in val)

    def __call__(self, *args, **kwargs):
        if all((self.check_args(args), self.check_args(kwargs))):
            return self.func(*args, **kwargs)
        else:
            raise TypeError('Аргументы должны принадлежать типам int или float')


# test 1

@takes_numbers
def mul(a, b):
    return a * b


print(mul(1, 2))
print(mul(1, 2.5))
print(mul(1.5, 2))
print(mul(1.5, 2.5))
print()

# test 2

@takes_numbers
def mul(a, b):
    return a * b


try:
    print(mul(1, '2'))
except TypeError as error:
    print(error)








