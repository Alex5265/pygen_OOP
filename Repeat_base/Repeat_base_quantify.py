# Функция quantify()
# Реализуйте функцию quantify(), которая принимает два аргумента в следующем порядке:
#
# iterable — итерируемый объект
# predicate — функция-предикат, то есть функция, возвращающая True или False. Если имеет значение None, то работает аналогично функции bool()
# Функция quantify() должна считать, для скольких элементов итерируемого объекта iterable функция-предикат predicate вернула значение True, и возвращать полученный результат.
#
# Примечание 1. Рассмотрим первый тест, в котором в качестве итерируемого объекта передается список чисел от 1 до 10, в качестве функции-предиката — функция, возвращающая True, если аргумент больше единицы, или False в противном случае. Переданный список чисел содержит ровно 9 чисел, больших единицы.
#
# Примечание 2. В тестирующую систему сдайте программу, содержащую только необходимую функцию quantify(), но не код, вызывающий ее.



def quantify(iterable, predicate):
    if predicate is None:
        predicate = bool
    return sum(map(predicate, iterable))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(quantify(numbers, lambda x: x > 1))


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(quantify(numbers, lambda x: x < 0))









