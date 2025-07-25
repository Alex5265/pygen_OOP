# Класс Suppress
# Реализуйте класс Suppress. При создании экземпляра класс должен принимать произвольное количество позиционных аргументов, каждый из которых представляет собой тип исключения.
#
# Экземпляр класса Suppress должен являться контекстным менеджером, подавляющим исключение, если оно возбуждается во время выполнения кода внутри блока with. Подавляться должны исключения тех типов, которые были перечислены при создании контекстного менеджера.
#
# Также экземпляр класса Suppress должен иметь один атрибут:
#
# exception — исключение, которое было подавлено контекстным менеджером. Если исключение не было подавлено или код был выполнен без исключений, атрибут должен иметь значение None
# Примечание 1. Наглядные примеры использования класса Suppress продемонстрированы в тестовых данных.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 3. Класс Suppress должен удовлетворять протоколу контекстного менеджера, то есть иметь методы __enter__() и __exit__(). Реализация же протокола может быть произвольной.


class Suppress:
    def __init__(self, *args):
        self.args = args
        self.exception = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type in self.args:
            self.exception = exc_val
            return True
        return False


with Suppress(TypeError, ValueError) as context:
    number = int('я число')

print(context.exception)
print(type(context.exception))









