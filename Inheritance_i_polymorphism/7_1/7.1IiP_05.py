# Классы Validator и NumberValidator
# Реализуйте класс Validator, описывающий объект, проверяющий значение на корректность. При создании экземпляра класс должен принимать один аргумент:
#
# obj — произвольный объект
# Класс Validator должен иметь один метод экземпляра:
#
# is_valid() — пустой метод, всегда возвращающий значение None
# Также реализуйте класс NumberValidator, наследника класса Validator, описывающий объект, проверяющий значение на принадлежность типу int или float. Процесс создания экземпляра класса NumberValidator должен совпадать с процессом создания экземпляра класса Validator.
#
# Класс NumberValidator должен иметь один метод экземпляра:
#
# is_valid() — метод, возвращающий True, если значение переданное в инициализатор принадлежит типу int или float, или False в противном случае
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализации классов нет, она может быть произвольной.


class Validator:
    def __init__(self, obj):
        self.obj = obj

    def is_valid(self):
        return None

class NumberValidator(Validator):
    def is_valid(self):
        return isinstance(self.obj, (int,float))


print(issubclass(NumberValidator, Validator))
print()

validator1 = Validator('beegeek')
validator2 = Validator(1)
validator3 = Validator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())
print()

validator1 = NumberValidator('beegeek')
validator2 = NumberValidator(1)
validator3 = NumberValidator(1.1)

print(validator1.is_valid())
print(validator2.is_valid())
print(validator3.is_valid())

















