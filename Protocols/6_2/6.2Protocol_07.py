# Класс HistoryDict 🌶️
# Реализуйте класс HistoryDict, описывающий словарь, который запоминает предыдущие значения по каждому ключу. При создании экземпляра класс должен принимать один аргумент:
#
# data — словарь, определяющий начальный набор элементов экземпляра класса HistoryDict. Если не передан, начальный набор элементов считается пустым
# Класс HistoryDict должен иметь пять методов экземпляра:
#
# keys() — метод, возвращающий итерируемый объект, элементами которого являются ключи экземпляра класса HistoryDict
# values() — метод, возвращающий итерируемый объект, элементами которого являются значения ключей экземпляра класса HistoryDict
# items() — метод, возвращающий итерируемый объект элементами которого являются элементы экземпляра класса HistoryDict в виде кортежей (<ключ>, <значение>)
# history() — метод, принимающий в качестве аргумента ключ и возвращающий список, элементами которого являются все значения, которые когда-либо содержались в экземпляре класса HistoryDict по указанному ключу. Если данный ключ не содержится в экземпляре класса HistoryDict (был удален или никогда не добавлялся), метод должен вернуть пустой список
# all_history() — метод, возвращающий словарь, ключами в котором являются ключи экземпляра класса HistoryDict, а значениями — списки, содержащие все значения, которые когда-либо содержались по этим ключам. Если какой-либо ключ был удален из экземпляра класса HistoryDict, то считается, что была удалена и его история
# При передаче экземпляра класса HistoryDict в функцию len() должно возвращаться количество элементов в нем.
#
# Также экземпляр класса HistoryDict должен быть итерируемым объектом, то есть позволять перебирать свои ключи, например, с помощью цикла for.
#
# Наконец, экземпляр класса HistoryDict должен позволять получать и изменять значения своих элементов по их ключам, добавлять новые пары (ключ, значение) и удалять уже имеющиеся.
#
# Примечание 1. Экземпляр класса HistoryDict не должен зависеть от словаря, на основе которого он был создан. Другими словами, если исходный словарь изменится, то экземпляр класса HistoryDict измениться  не должен.
#
# Примечание 2. Реализация класса HistoryDict может быть произвольной, то есть требований к наличию определенных атрибутов нет.
#
# Примечание 3. Дополнительная проверка данных на корректность в методах не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
import copy


class HistoryDict:
    def __init__(self, data=None):
        if data is None:
            self.data = {}
        else:
            self.data = {key:[value] for key, value in data.items()}

    def __len__(self):
        return len(self.data)

    def __getitem__(self, item):
        return self.data.get(item)[-1]

    def __setitem__(self, key, value):
        if key in self.data:
            self.data[key].append(value)
        else:
            self.data.update({key:[value]})

    def __delitem__(self, key):
        self.data.pop(key, None)

    def __iter__(self):
        return iter(self.data.keys())

    def keys(self):
        return tuple(k for k in self.data.keys())

    def values(self):
        return tuple(v[-1] for v in self.data.values())

    def items(self):
        return tuple((k, v[-1]) for k, v in self.data.items())

    def history(self, key):
        return self.data.get(key, [])

    def all_history(self):
        return self.data






# historydict = HistoryDict({'ducks': 99, 'cats': 1})
#
# print(historydict['ducks'])
# print(historydict['cats'])
# print(len(historydict))
# print()
#
#
# historydict = HistoryDict({'ducks': 99, 'cats': 1})
#
# print(*historydict)
# print(*historydict.keys())
# print(*historydict.values())
# print(*historydict.items())
# print()
#
# historydict = HistoryDict({'ducks': 99, 'cats': 1})
#
# historydict['ducks'] = 100
# print(historydict.history('ducks'))
# print(historydict.history('cats'))
# print(historydict.history('dogs'))
# print()
#
# historydict = HistoryDict({'ducks': 99, 'cats': 1})
#
# print(historydict.all_history())
# historydict['ducks'] = 100
# historydict['ducks'] = 101
# historydict['cats'] = 2
# print(historydict.all_history())
# print()
#
#
# historydict = HistoryDict({'ducks': 99, 'cats': 1})
#
# historydict['dogs'] = 1
# print(len(historydict))
# del historydict['ducks']
# del historydict['cats']
# print(len(historydict))


historydict = HistoryDict()
print('Keys:', *historydict.keys())
print('Values:', *historydict.values())
print('Items:', *historydict.items())
print('History(key=1):', historydict.history(1))
print('History(key=1):', historydict.history(1))
print('All history:', historydict.all_history())


