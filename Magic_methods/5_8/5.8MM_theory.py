class Cat:
    def __init__(self, name):
        self.name = name  # имя кошки

    def __getattribute__(self, attr):
        print(f'Возвращаю значение атрибута {attr}')
        return object.__getattribute__(self, attr)  # получение значения атрибута attr объекта self


cat = Cat('Кемаль')
print('строка перед вызовом атт')
print(cat.name)

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed  # порода кошки

    def __getattr__(self, attr):
        if attr == 'info':
            return f'Имя: {self.name}\nПорода: {self.breed}'
        raise AttributeError


cat = Cat('Кемаль', 'Британский')

print(cat.info)

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __setattr__(self, attr, value):
        attr = '_' + attr
        self.__dict__[attr] = value


cat = Cat('Кемаль', 'Британский')

print(cat.__dict__)


class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __setattr__(self, attr, value):
        print(f'Устанавливаю атрибуту {attr} значение {value}')
        attr = '_' + attr
        self.attr = value


cat = Cat('Кемаль', 'Британский')

print(cat.__dict__)

class Cat:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def __delattr__(self, attr):
        print(f'Удаляю атрибут {attr}')
        del self.__dict__[attr]


cat = Cat('Кемаль', 'Британский')

print(cat.__dict__)
del cat.name
print(cat.__dict__)

del cat.breed
print(cat.__dict__)

class Cat:
    def __getattribute__(self, attr):
        print(f'Возвращаю значение атрибута {attr}')
        return object.__getattribute__(self, attr)

    def __getattr__(self, attr):
        print(f'Возвращаю значение по умолчанию')
        return None

    def __setattr__(self, attr, value):
        print(f'Устанавливаю атрибуту {attr} значение {value}')
        self.__dict__[attr] = value

    def __delattr__(self, attr):
        print(f'Удаляю атрибут {attr}')
        del self.__dict__[attr]


cat = Cat()

setattr(cat, 'name', 'Кемаль')
print()
getattr(cat, 'name')
print()
getattr(cat, 'breed')
print()
delattr(cat, 'name')
