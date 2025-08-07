# Декоратор @jsonattr
# Реализуйте декоратор @jsonattr для декорирования класса. Декоратор должен принимать один аргумент:
#
# filename — имя json файла, содержимым которого является JSON объект
# Декоратор должен открывать файл filename и добавлять в качестве атрибута декорируемому классу каждую пару ключ-значение JSON объекта, содержащегося в этом файле.
import functools
import json

def jsonattr(filename):
    def wrapper(cls):
        old_init = cls.__init__
        with open(filename, 'r') as file:
            for k, v in json.load(file).items():
                setattr(cls, k, v)

        @functools.wraps(old_init)
        def new_init(self, *args, **kwargs):
            old_init(self, *args, **kwargs)

        cls.__init__ = new_init
        return cls

    return wrapper


# test 1

with open('test.json', 'w') as file:
    file.write('{"x": 1, "y": 2}')


@jsonattr('test.json')
class MyClass:
    pass


print(MyClass.x)
print(MyClass.y)








