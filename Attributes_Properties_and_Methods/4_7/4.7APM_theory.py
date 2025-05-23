class Cat:
    def __init__(self, breed, name):
        self.breed = breed
        self.name = name

    @classmethod
    def british(cls, name):
        return cls('Британский', name)                       # равнозначно Cat('Британский', name)


cat = Cat.british('Кемаль')
cat1 = Cat('вислоухий','кота')
cat2 = Cat.british('SimSim')

print(cat.breed, cat.name)
print(cat1.breed, cat1.name)
print(cat2.breed, cat2.name)


class MyClass:
    @staticmethod
    def my_staticmethod():
        print('Это статический метод')


MyClass.my_staticmethod()


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self, in_human_years=False):
        if in_human_years:
            return Cat.age_in_human_years(self.age)          # переводим кошачьи года в человеческие
        return self.age

    @staticmethod
    def age_in_human_years(age):
        return (age + (age < 5) - (age > 8)) * 7             # переводим кошачьи года в человеческие


cat = Cat('Кемаль', 2)

print(cat.get_age())                                         # возраст в кошачьих годах
print(cat.get_age(True))                                     # возраст в человеческих годах



class MyClass:
    def method(self):
        print('Это метод экземпляра')
        print(self)
        print(self.__class__)


obj = MyClass()

obj.method()


class MyClass:
    @classmethod
    def my_classmethod(cls):
        print('Это метод класса')
        print(cls)

    @staticmethod
    def my_staticmethod():
        print('Это статический метод')


obj = MyClass()

obj.my_classmethod()
obj.my_staticmethod()
