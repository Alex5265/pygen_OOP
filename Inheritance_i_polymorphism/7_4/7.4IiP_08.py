# Класс MutableString
# Реализуйте класс MutableString, наследника класса UserString, описывающий изменяемую строку. Процесс создания экземпляра класса MutableString должен совпадать с процессом создания экземпляра класса UserString.
#
# Класс MutableString должен иметь три метода экземпляра:
#
# lower() — метод, переводящий все символы изменяемой строки в нижний регистр
# upper() — метод, переводящий все символы изменяемой строки в верхний регистр
# sort() — метод, сортирующий символы изменяемой строки. Может принимать два необязательных именованных аргумента key и reverse, выполняющих ту же задачу, что и в функции sorted()
# Экземпляр класса MutableString должен позволять получать, изменять и удалять значения своих элементов с помощью индексов, причем как положительных, так и отрицательных.
#
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализации класса MutableString нет, она может быть произвольной.

from collections import UserString


class MutableString(UserString):
    def __setitem__(self, index, value):
        data_as_list = list(self.data)
        data_as_list[index] = value
        self.data = "".join(data_as_list)

    def __delitem__(self, index):
        data_as_list = list(self.data)
        del data_as_list[index]
        self.data = "".join(data_as_list)

    def upper(self):
        self.data = self.data.upper()

    def lower(self):
        self.data = self.data.lower()

    def sort(self, key=None, reverse=False):
        self.data = "".join(sorted(self.data, key=key, reverse=reverse))


mutablestring = MutableString('Beegeek')

mutablestring.lower()
print(mutablestring)
mutablestring.upper()
print(mutablestring)
mutablestring.sort()
print(mutablestring)
print()

mutablestring = MutableString('beegeek')

print(mutablestring)
mutablestring[0] = 'B'
mutablestring[-4] = 'G'
print(mutablestring)









