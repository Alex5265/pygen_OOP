# Класс SparseArray
# Разреженный массив (список) — абстрактное представление обычного массива (списка), в котором данные представлены не непрерывно, а фрагментарно: большинство его элементов принимает одно и то же значение по умолчанию, обычно 0 или None. В разреженном массиве возможен доступ к неопределенным элементам, в этом случае массив вернет некоторое значение по умолчанию.
#
# Реализуйте класс SparseArray, описывающий разреженный массив. При создании экземпляра класс должен принимать один аргумент:
#
# default — значение по умолчанию для неопределенных элементов разреженного массива
# Экземпляр класса SparseArray должен позволять получать и изменять значения своих элементов с помощью индексов. При попытке получить значение элемента по несуществующему индексу должно быть возвращено значение по умолчанию.
#
# Примечание 1. Гарантируется, что при доступе к элементам используются только неотрицательные индексы.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 3. Никаких ограничений касательно реализации класса SparseArray нет, она может быть произвольной.


class SparseArray:
    def __init__(self, default):
        self.array = {}
        self.default = default

    def check_key(self, key):
        if not isinstance(key, int):
            raise TypeError
        return key

    def __setitem__(self, key, value):
        key = self.check_key(key)
        self.array[key] = value

    def __len__(self):
        if not self.array:
            return 0
        else:
            return max(self.array)

    def __getitem__(self, item):
        return self.array.get(item, self.default)

    def __iter__(self):
        yield from self.array.values()

    def __contains__(self, item):
        return item in self.array


array = SparseArray(0)


array[5] = 1000
array[12] = 1001

print(array[5])
print(array[12])
print(array[13])
print()


array = SparseArray(None)

array[0] = 'Timur'
array[1] = 'Arthur'

print(array[0])
print(array[1])
print(array[2])






