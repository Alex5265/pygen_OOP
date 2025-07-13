# Класс TwoWayDict
# Реализуйте класс TwoWayDict, наследника класса UserDict, описывающий двунаправленный словарь, в который при добавлении пары ключ: значение также добавляется и пара значение: ключ. Процесс создания экземпляра класса TwoWayDict должен совпадать с процессом создания экземпляра класса UserDict.
#
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализации класса TwoWayDict нет, она может быть произвольной.
from collections import UserDict

class TwoWayDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key,value)
        super().__setitem__(value, key)




twowaydict = TwoWayDict({'apple': 1})

twowaydict['banana'] = 2

print(twowaydict['apple'])
print(twowaydict[1])
print(twowaydict['banana'])
print(twowaydict[2])
print()

d = TwoWayDict()
d[3] = 8
d[7] = 6
print(d[3], d[8])
print(d[7], d[6])

d.update({9: 7, 8: 2})
print(d[9], d[7])
print(d[8], d[2])










