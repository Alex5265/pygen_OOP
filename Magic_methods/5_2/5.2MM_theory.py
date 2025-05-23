# from datetime import date
#
# dt = date(2022, 10, 23)
#
# dt_str = str(dt)
# dt_repr = repr(dt)
#
# print(dt_str, type(dt_str))
# print(dt_repr, type(dt_repr))


# import datetime
#
# dt1 = datetime.date(2022, 10, 23)
# dt2 = eval(repr(dt1))
#
# print(dt2)
# print(type(dt2))
#
#
class MyClass:
    pass


obj = MyClass()

print(str(obj))
print(repr(obj))


class Cat:
    def __init__(self, name):
        self.name = name                        # имя кошки

    def __str__(self):
        return f'Кот по имени {self.name}'

    def __repr__(self):
        return f"Cat('{self.name}')"


cat = Cat('Кемаль')

print(str(cat))
print(repr(cat))

cat1 = repr(cat)
print(type(cat1))
cat1 = eval(cat1)
print(type(cat1))
print(cat1.__dict__)








