# print(hash(1))                          # хеш-значение целого числа
# print(hash(2.5))                        # хеш-значение вещественного числа
# print(hash('bee'))                      # хеш-значение строки
# print(hash((1, 2, 3)))                  # хеш-значение кортежа
#
# print(hash(1))
# print(hash(69))
# print(hash(314))
# print(hash(2077))
# print(hash(-1))
#
#
# print(hash('beegeek'))
# print(hash('beegeek'))
# print(hash('beegeek!'))
# print(hash('beek'))
# print(hash('geek'))


# def hash_function(obj):
#     return hash(obj) % 100
#
# data = [2077, 3.14, 'bee', 'geek', (1, 2, 3)]
#
# for obj in data:
#     print(hash_function(obj))
#
#
# from time import perf_counter
#
# start = perf_counter()
#
# hash('b' * 100_000_000)
#
# end = perf_counter()
# print(end - start)


from collections import defaultdict
from string import printable

hashes = defaultdict(int)

for char in printable:
    hashes[hash(char) % 20] += 1

for hash_value, hash_count in sorted(hashes.items()):
    print(hash_value, '■' * hash_count)

print('')
