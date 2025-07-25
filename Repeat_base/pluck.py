# Реализуйте функцию pluck(), которая принимает три аргумента в следующем порядке:
#
# data — словарь произвольной вложенности
# path — строка, представляющая собой ключ или последовательность ключей, перечисленных через точку .
# default — произвольный объект, значение по умолчанию; имеет значение None, если не передан явно
# Функция должна возвращать значение по ключу path из словаря data. Если path представляет собой последовательность ключей, например, key1.key2, то возвращаемым значением функции должно быть значение по ключу key2 из словаря data[key1]. Если указанного ключа или хотя бы одного ключа из последовательности ключей в словаре нет, функция должна вернуть значение default.
#
# Примечание 1. В тестирующую систему сдайте программу, содержащую только необходимую функцию pluck(), но не код, вызывающий ее.


# def pluck(data:dict, path:str, default=None):
#     path = path.split('.')
#     if len(path) < 2:
#         return data.setdefault(path[0], default)
#     if path[0] in data:
#         res = pluck(data[path[0]], '.'.join(path[1:]), default)
#         return res


# другое решение
def pluck(data, path, default=None):
    for key in path.split('.'):
        if isinstance(data, dict) and key in data:
            data = data[key]
        else:
            return default
    return data



d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'x'))

d = {'a': {'b': 5, 'z': 20}, 'c': {'d': 3}, 'x': 40}

print(pluck(d, 'a.b'))

d = {'a': {'b': {'c': {'d': {'e': 4}}}}}

print(pluck(d, 'a.b.c'))


