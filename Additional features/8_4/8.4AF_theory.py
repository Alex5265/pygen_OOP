import functools

def do_twice(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for _ in range(2):
            value = func(*args, **kwargs)
        return value
    return wrapper

@do_twice
def greet(name):
    print(f'Привет, {name}!')


greet('Кемаль')
print()



import functools

def do_n_times(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator

@do_n_times(4)
def greet(name):
    print(f'Привет, {name}!')


greet('Кемаль')
print()



import functools

def do_n_times(n):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(n):
                value = func(*args, **kwargs)
            return value
        return wrapper
    return decorator

class Cat:
    @do_n_times(4)
    def say(self):
        print('Мяу')


cat = Cat()
cat.say()
print()
print()


class do_twice:
    def __init__(self, func):
        self.func = func  # декорируемая функция

    def __call__(self, *args, **kwargs):
        for _ in range(2):
            value = self.func(*args, **kwargs)  # вызов декорируемой функции
        return value


def greet(name):
    print(f'Привет, {name}!')


greet = do_twice(greet)

greet('Кемаль')
print()

import functools


class do_twice:
    def __init__(self, func):
        functools.update_wrapper(self, func)  # сохранение информации о декорируемой функции
        self.func = func

    def __call__(self, *args, **kwargs):
        for _ in range(2):
            value = self.func(*args, **kwargs)
        return value


@do_twice
def greet(name):
    """docstring"""
    print(f'Привет, {name}!')


print(greet.__name__)
print(greet.__doc__)
print()

import functools


class do_n_times:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):  # передача декорируемой функции
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(self.n):
                value = func(*args, **kwargs)  # вызов декорируемой функции
            return value

        return wrapper


def greet(name):
    print(f'Привет, {name}!')


decorator = do_n_times(4)  # создание экземпляра класса do_n_times
greet = decorator(greet)  # вызов экземпляра класса do_n_times

greet('Кемаль')

print()

import functools


class do_n_times:
    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(self.n):
                value = func(*args, **kwargs)
            return value

        return wrapper


@do_n_times(4)
def greet(name):
    print(f'Привет, {name}!')


greet('Кемаль')























