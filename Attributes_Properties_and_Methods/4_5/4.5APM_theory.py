class Cat:
    def __init__(self, name):
        self._name = name

    def get_name(self):
        print(f'Возвращаю имя {self._name}')
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

    name = property(get_name, set_name)


cat1 = Cat('Кемаль')
cat2 = Cat('Роджер')

print(cat1.name)
print(cat2.name)



cat3 = Cat('Кемаль')
try:
    cat3.name = 1
except ValueError as e:
    print(e)

print()


class Cat:
    def __init__(self, name):
        self.name = name                              # обращение к свойству name

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and name.isalpha():
            self._name = name
        else:
            raise ValueError('Некорректное имя')

    name = property(get_name, set_name)


try:
    cat = Cat(-1)
except ValueError as e:
    print(e)

