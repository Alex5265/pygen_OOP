# Декоратор @ignore_exception
# Реализуйте класс декоратор @ignore_exception, который принимает произвольное количество позиционных аргументов — типов исключений, и выводит текст:
#
# Исключение <тип исключения> обработано
# если во время выполнения декорируемой функции было возбуждено исключение, принадлежащее одному из переданных типов. Если возбужденное исключение не принадлежит ни одному из переданных типов, оно должно быть возбуждено снова.
#
# Примечание 1. Не забывайте про то, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @ignore_exception, но не код, вызывающий его.
import functools

class ignore_exception:
    def __init__(self, *exception):
        self.exception = exception

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as error:
                if not type(error) in self.exception:
                    raise error
                print(f'Исключение {type(error).__name__} обработано')
        return wrapper


# test 1


@ignore_exception(ZeroDivisionError, TypeError, ValueError)
def func(x):
    return 1 / x


func(0)
print()

# test 2

min = ignore_exception(ZeroDivisionError)(min)

try:
    print(min(1, '2', 3, [4, 5]))
except Exception as error:
    print(type(error))

print()

# test 8

@ignore_exception(ValueError, TypeError, ZeroDivisionError, NameError)
def beegeek():
    """beegeek"""
    return 'beegeek'


print(beegeek.__name__)
print(beegeek.__doc__)
print(beegeek())





