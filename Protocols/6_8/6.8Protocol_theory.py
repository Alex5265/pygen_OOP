# from contextlib import closing
#
#
# class Cat:
#     def __init__(self, name):
#         self.name = name
#
#     def __str__(self):
#         return self.name
#
#     def close(self):
#         print('Пока,', self.name)
#
#
# with closing(Cat('Кемаль')) as cat:
#     print('Привет,', cat)
#
# print()
#
# from contextlib import suppress
#
# with suppress(ValueError):
#     num = int('python')
#
# print('beegeek')
#
# with suppress(TypeError, ZeroDivisionError):
#     num = 1 / 0
#
# print('pygen')
# print()
#
# from contextlib import redirect_stdout
#
# with open('output.txt', mode='w', encoding='utf-8') as file:
#     with redirect_stdout(file):
#         print('Python generation!')
#         help(len)


# from contextlib import ExitStack
#
#
# class Greeter:
#     def __init__(self, name):
#         self.name = name
#
#     def __enter__(self):
#         print('Привет,', self.name)
#         return self.name
#
#     def __exit__(self, *args, **kwargs):
#         print('Пока,', self.name)
#
#
# with ExitStack() as stack:
#     stack.enter_context(Greeter('Гвидо'))
#     stack.enter_context(Greeter('Трей'))
#     print('Завершение блока with')




# class Cat:
#     def __init__(self, name):
#         self._name = name
#
#     @property
#     def name(self):
#         print('Получение значения атрибута name')
#         return self._name
#
#     @name.setter
#     def name(self, value):
#         print('Изменение значения атрибута name')
#         if isinstance(value, str) and len(value) > 0:
#             self._name = value
#         else:
#             raise ValueError('Некорректное имя')
#
#     @name.deleter
#     def name(self):
#         print('Удаление атрибута name')
#         del self._name
#
#
# cat = Cat('Кемаль')
# name_property = Cat.name                   # свойство name, он же объект типа property, он же дескриптор
#
# name_property.__get__(cat, Cat)            # равнозначно cat.name
# name_property.__set__(cat, 'Роджер')       # равнозначно cat.name = 'Роджер'
# name_property.__delete__(cat)              # равнозначно del cat.name


# class NonEmptyString:
#     def __init__(self, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         print('Вызов метода __get__()')
#         if self._attr in obj.__dict__:
#             return obj.__dict__[self._attr]
#         else:
#             raise AttributeError('Атрибута не существует')
#
#     def __set__(self, obj, value):
#         print('Вызов метода __set__()')
#         if isinstance(value, str) and len(value) > 0:
#             obj.__dict__[self._attr] = value
#         else:
#             raise ValueError('Некорректное значение')
#
#     def __delete__(self, obj):
#         print('Вызов метода __delete__()')
#         del obj.__dict__[self._attr]
#
#
# class Cat:
#     name = NonEmptyString('name')
#
#     def __init__(self, name):
#         self.name = name
#
#
# cat = Cat('Кемаль')
#
# cat.name
# cat.name = 'Роджер'
# del cat.name


# class NonEmptyString:
#     def __set_name__(self, cls, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         if self._attr in obj.__dict__:
#             return obj.__dict__[self._attr]
#         else:
#             raise AttributeError('Атрибута не существует')
#
#     def __set__(self, obj, value):
#         if isinstance(value, str) and len(value) > 0:
#             obj.__dict__[self._attr] = value
#         else:
#             raise ValueError('Некорректное значение')
#
#     def __delete__(self, obj):
#         del obj.__dict__[self._attr]
#
#
# class Cat:
#     name = NonEmptyString()  # строка 'name' автоматически передается в метод __set_name__()
#
#     def __init__(self, name):
#         self.name = name
#
#
# cat = Cat('Кемаль')
# print(cat.name)
#
# cat.name = 'Роджер'
# print(cat.name)
#
# del cat.name
# print(hasattr(cat, 'name'))



# class NonEmptyString:
#     def __set_name__(self, cls, attr):
#         self._attr = attr
#
#     def __get__(self, obj, cls):
#         print('Вызов метода __get__()')
#         if self._attr in obj.__dict__:
#             return obj.__dict__[self._attr]
#         else:
#             raise AttributeError('Атрибута не существует')
#
#     def __set__(self, obj, value):
#         if isinstance(value, str) and len(value) > 0:
#             obj.__dict__[self._attr] = value
#         else:
#             raise ValueError('Некорректное значение')
#
# class Cat:
#     name = NonEmptyString()
#
#     def __init__(self, name):
#         self.name = name
#
#
# cat = Cat('Кемаль')
#
# print(cat.name)
# print(cat.__dict__)
# print(Cat.__dict__)

# class Descriptor:
#     def __get__(self, obj, cls):
#         print('Вызов метода __get__()')
#         print(obj, cls)
#
# class Cat:
#     name = Descriptor()
#
#
# Cat.name


class NonEmptyString:
    def __set_name__(self, cls, attr):
        self.attr = attr

    def __get__(self, obj, cls):
        if obj is None:                    # проверка на то, как осуществляется обращение
            return self
        if self.attr in obj.__dict__:
            return obj.__dict__[self.attr]
        else:
            raise AttributeError('Атрибута не существует')

    def __set__(self, obj, value):
        if isinstance(value, str) and len(value) > 0:
            obj.__dict__[self.attr] = value
        else:
            raise ValueError('Некорректное значение')

class Cat:
    name = NonEmptyString()

    def __init__(self, name):
        self.name = name


cat = Cat('Кемаль')

print(cat.name)
print(Cat.name)


class NonEmptyString:
    def __set_name__(self, cls, attr):
        self.attr = attr

    def __get__(self, obj, cls):
        if self.attr in obj.__dict__:
            return obj.__dict__[self.attr]
        else:
            raise AttributeError('Атрибута не существует')

    def __set__(self, obj, value):
        if isinstance(value, str) and len(value) > 0:
            obj.__dict__[self.attr] = value
        else:
            raise ValueError('Некорректное значение')

class Cat:
    name = NonEmptyString()

    def __init__(self, name):
        self.name = name


cat = Cat('Кемаль')

print(cat.name)
print(Cat.name)



class Integer:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        print(f'__get__:{self.name}')
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        print(f'__set__:{self.name} = {value}')
        instance.__dict__[self.name] = value


class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


p = Point3D(2,5,9)
print(p.x)
print(p.__dict__)



