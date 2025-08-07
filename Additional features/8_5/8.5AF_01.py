# Декоратор @track_instances
# Реализуйте декоратор @track_instances для декорирования класса. Декоратор должен добавлять декорируемому классу атрибут instances, содержащий список всех созданных экземпляров этого класса.
#
# Примечание 1. Экземпляры декорируемого класса в списке по атрибуту instances должны располагаться в том порядке, в котором они были созданы.
import functools


def track_instances(cls):
    old_init = cls.__init__
    cls.instances = []

    @functools.wraps(old_init)
    def new_init(self, *args, **kwargs):
        old_init(self, *args, **kwargs)
        cls.instances.append(self)

    cls.__init__ = new_init
    return cls





# test 1

@track_instances
class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f'Person({self.name!r})'


obj1 = Person('object 1')
obj2 = Person('object 2')

print(Person.instances)









