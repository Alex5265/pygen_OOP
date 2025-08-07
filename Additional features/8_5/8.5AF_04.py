# Декоратор @singleton
# Реализуйте декоратор @singleton для декорирования класса. Декоратор должен превращать декорируемый класс в синглтон, то есть в класс, при первом вызове создающий единственный свой экземпляр и при последующих вызовах возвращающий его же.
#
# Примечание 1. Подробнее почитать про шаблон проектирования синглтон можно по ссылке.

import functools


def singleton(cls):
    cls_new = cls.__new__
    cls._instance = None

    @functools.wraps(cls_new)
    def new_for_singleton(*args, **kwargs):
        if cls._instance is None:
            cls._instance = object.__new__(cls)
        return cls._instance

    cls.__new__ = new_for_singleton
    return cls


# test 1

@singleton
class MyClass:
    pass


obj1 = MyClass()
obj2 = MyClass()

print(obj1 is obj2)



