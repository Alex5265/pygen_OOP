# Декоратор @snake_case
# Snake Case — стиль написания составных слов, при котором несколько слов разделяются символом нижнего подчеркивания (_) и не имеют пробелов в записи, причём каждое слово пишется с маленькой буквы. Например, bee_geek и hello_world.
#
# Camel Case — стиль написания составных слов, при котором несколько слов пишутся слитно без пробелов, при этом каждое слово пишется с заглавной буквы. Например, BeeGeek и HelloWorld.
#
# Частным случаем стиля Camel Case является lower Camel Case, когда с заглавной буквы пишутся все слова, кроме первого. Например, beeGeek и helloWorld.
#
# Реализуйте декоратор @snake_case для декорирования класса. Декоратор должен принимать один аргумент:
#
# attrs — булево значение, по умолчанию равняется False
# Декоратор должен переименовывать все не магические методы в декорируемом классе, меняя их стиль написания c Camel Case и lower Camel Case на Snake Case. Параметр attrs должен определять, будут ли аналогичным образом переименованы атрибуты класса. Если он имеет значение True, стиль написания имен атрибутов класса должен поменяться с Camel Case и lower Camel Case на Snake case, если False — остаться прежним.
#
# Примечание 1. Гарантируется, что имена всех не магических методов и атрибутов в классе написаны в стилях Camel Case, lower Camel Case или Snake Case.

import re
from typing import Callable


def snake_case(attrs=False):
    regex_object = re.compile(r'_?\B([A-Z])')

    def wrapper(cls, *args, **kwargs):
        class_attributes = list(cls.__dict__.keys())
        for attribute in class_attributes:
            if any((
                    attribute.startswith('__') and attribute.endswith('__'),
                    not isinstance(cls.__dict__[attribute], Callable) and not attrs
            )):
                continue
            setattr(cls, regex_object.sub(r'_\1', attribute).lower(), cls.__dict__[attribute])
            delattr(cls, attribute)
        return cls

    return wrapper


# test 1

@snake_case()
class MyClass:
    def FirstMethod(self):
        return 1

    def superSecondMethod(self):
        return 2


obj = MyClass()

print(obj.first_method())
print(obj.super_second_method())
print()


# test 2

@snake_case(attrs=True)
class MyClass:
    FirstAttr = 1
    superSecondAttr = 2

print(MyClass.first_attr)
print(MyClass.super_second_attr)
print()


# test 3

@snake_case()
class MyClass:
    FirstAttr = 1

    def FirstMethod(self):
        return 1


obj = MyClass()

print(MyClass.FirstAttr)
print(obj.first_method())




