class Cat:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):                  # первое свойство name, доступное только для чтения
        return self._name

    @name.setter
    def set_name(self, name):        # второе свойство set_name, доступное для чтения и записи
        self._name = name

    @name.deleter
    def del_name(self):              # третье свойство del_name, доступное для чтения и удаления
        del self._name


cat = Cat('Кемаль')

print(cat.name)
print(cat.set_name)
print(cat.del_name)