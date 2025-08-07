def add_attr(cls):
    cls.attr = None                                 # добавляем декорируемому классу атрибут attr
    return cls                                      # возвращаем декорируемый класс

@add_attr
class MyClass:
    pass


print(MyClass.attr)
print()

import functools


def add_attr_to_instances(cls):
    old_init = cls.__init__  # сохраняем исходный инициализатор

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)  # вызываем исходный инициализатор
        self.attr = None  # добавляем экземпляру класса атрибут attr

    cls.__init__ = new_init  # заменяем исходный инициализатор новым
    return cls


@add_attr_to_instances
class MyClass:
    pass


obj = MyClass()

print(obj.attr)
print()

import functools


def add_attr_to_instances(**attrs):
    def decorator(cls):
        old_init = cls.__init__

        @functools.wraps(old_init)
        def new_init(self, *args, **kwargs):
            old_init(self, *args, **kwargs)
            self.__dict__.update(attrs)  # добавляем атрибуты экземпляру декорируемого класса

        cls.__init__ = new_init
        return cls

    return decorator


@add_attr_to_instances(first_attr=1, second_attr=2)
class MyClass:
    pass


obj = MyClass()

print(obj.first_attr)
print(obj.second_attr)
print()

import functools


def count_instances(cls):
    old_init = cls.__init__
    cls.count = 0  # счетчик созданных экземпляров декорируемого класса

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.count += 1  # увеличение счетчика на единицу

    cls.__init__ = new_init
    return cls


@count_instances
class MyClass:
    pass


print(MyClass.count)

for _ in range(10):
    obj = MyClass()

print(MyClass.count)














