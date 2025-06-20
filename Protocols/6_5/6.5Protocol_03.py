# Класс Closer
# Реализуйте класс Closer. При создании экземпляра класс должен принимать один аргумент:
#
# obj — произвольный объект
# Экземпляр класса Closer должен являться контекстным менеджером, который закрывает используемый объект obj с помощью метода close() после выполнения кода внутри блока with. Если объект не поддерживает операцию закрытия, контекстный менеджер должен вывести:
#
# Незакрываемый объект
# Примечание 1. Наглядные примеры использования класса Closer продемонстрированы в тестовых данных.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 3. Класс Closer должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.



class Closer:
    def __init__(self, obj):
        self.obj = obj

    def __enter__(self):
        return self.obj

    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            self.obj.close()
        except:
            print('Незакрываемый объект')
        finally:
            return True




# output = open('output.txt', 'w', encoding='utf-8')
#
# with Closer(output) as file:
#     print(file.closed)
#
# print(file.closed)


from zipfile import ZipFile

zip_file = ZipFile('test.zip', 'w')

with Closer(zip_file) as zf:
    print(zf)

# unclosable = [3.14, 'Elon', {'Ч': 'LXXIV'}, [1, 2, 3], (4, 5, 6), True, False]
#
# for item in unclosable:
#     with Closer(item) as zf:
#         print(item)

