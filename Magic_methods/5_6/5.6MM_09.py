# Декоратор @CachedFunction
# Реализуйте декоратор @CachedFunction, который кэширует вычисленные значения декорируемой функции. Кэш должен быть доступен по атрибуту cache и представлять собой словарь, ключом в котором является кортеж с аргументами, а значением — возвращаемое значение декорируемой функции при вызове с этими аргументами.
#
# Примечание 1. Для однозначного кеширования гарантируется, что декорируемая функция принимает только позиционные аргументы.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимый декоратор @CachedFunction, но не код, вызывающий его.


class CachedFunction:
    def __init__(self, func):
        self.func = func
        self.cache = {}

    def __call__(self, *args):
        result = self.cache.get(args)
        if result is None:
            result =self.func(*args)
        self.cache.setdefault(args, result)
        return result


@CachedFunction
def slow_fibonacci(n):
    if n == 1:
        return 0
    elif n in (2, 3):
        return 1
    return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)


print(slow_fibonacci(100))
print()


# @CachedFunction
# def slow_fibonacci(n):
#     if n == 1:
#         return 0
#     elif n in (2, 3):
#         return 1
#     return slow_fibonacci(n - 1) + slow_fibonacci(n - 2)
#
#
# slow_fibonacci(5)
#
# for args, value in sorted(slow_fibonacci.cache.items()):
#     print(args, value)



