# Класс Numbers
# Реализуйте класс Numbers, описывающий изначально пустой расширяемый набор целых чисел. При создании экземпляра класс не должен принимать никаких аргументов.
#
# Класс Numbers должен иметь три метода экземпляра:
#
# add_number() — метод, принимающий в качестве аргумента целое число и добавляющий его в набор
# get_even() — метод, возвращающий список всех четных чисел из набора
# get_odd() — метод, возвращающий список всех нечетных чисел из набора
# Примечание 1. Числа в списках, возвращаемых методами get_even() и get_odd(), должны располагаться в том порядке, в котором они были добавлены в набор.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.


class Numbers:
    def __init__(self):
        self.numbers = []

    def add_number(self, num):
        self.numbers.append(num)

    def get_even(self):
        return list(filter(lambda i: i % 2 == 1, self.numbers))

    def get_odd(self):
        return list(filter(lambda i: i % 2 == 0, self.numbers))

numbers = Numbers()

numbers.add_number(3)
numbers.add_number(2)
numbers.add_number(1)
numbers.add_number(4)

print(numbers.get_even())
print(numbers.get_odd())

numbers = Numbers()

numbers.add_number(1)
numbers.add_number(3)
numbers.add_number(1)

print(numbers.get_even())
print(numbers.get_odd())