# Декоратор @type_check
# Реализуйте класс декоратор @type_check, который принимает один аргумент:
#
# types — список, элементами которого являются типы данных
# Декоратор должен проверять, что типы всех позиционных аргументов, передаваемых в декорируемую функцию, полностью сопоставляются с типами из списка types, то есть типом первого аргумента является первый элемент списка types, типом второго аргумента — второй элемент списка types, и так далее. Если данное условие не выполняется, должно быть возбуждено исключение TypeError.
#
# Если количество позиционных аргументов больше, чем количество элементов в списке types, то не сопоставляемые аргументы не должны учитываться при проверке. Если количество позиционных аргументов меньше чем количество элементов в списке types, то не сопоставляемые типы из списка types не должны учитываться при проверке.
#
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @type_check, но не код, вызывающий его.
import functools


class type_check:
    def __init__(self, arr_type):
        self.arr_type = arr_type

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for typ, arg in list(zip(self.arr_type, args)):
                if not isinstance(arg, typ):
                    raise TypeError
            return func(*args, **kwargs)
        return wrapper


# test 1

@type_check([int, int])
def add(a, b):
    return a + b

print(add(1, 2))
print()


# test 2


@type_check([int, int])
def add(a, b):
    return a + b

try:
    print(add(1, '2'))
except Exception as error:
    print(type(error))

# test 3

@type_check([int, int, str, list])
def add(a, b):
    """sum a and b"""
    return a + b

print(add.__name__)
print(add.__doc__)
print(add(1, 2))








