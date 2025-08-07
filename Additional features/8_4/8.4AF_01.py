# Декоратор @reverse_args
# Вам доступен декоратор @reverse_args, который передает все позиционные аргументы в декорируемую функцию в обратном порядке. Реализуйте декоратор @reverse_args в виде класса декоратора.
#
# Примечание 1. Не забывайте, что декоратор не должен поглощать возвращаемое значение декорируемой функции, а также должен уметь декорировать функции с произвольным количеством позиционных и именованных аргументов.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @reverse_args, но не код, вызывающий его.

import functools

def reverse_args(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args = reversed(args)
        return func(*args, **kwargs)
    return wrapper

# решение
import functools

class reverse_args:
    def __init__(self, func):
        functools.update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        r_args = reversed(args)
        value = self.func(*r_args, **kwargs)
        return value



# test 1


@reverse_args
def power(a, n):
    return a ** n


print(power(2, 3))
print()

# test 2
@reverse_args
def concat(a, b, c):
    return a + b + c


print(concat('apple', 'cherry', 'melon'))






