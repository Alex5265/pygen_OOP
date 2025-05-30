# Класс Book
# Требовалось реализовать класс Book, описывающий книгу. При создании экземпляра класс должен был принимать три аргумента в следующем порядке:
#
# title — название книги
# author — автор книги
# year — год выпуска книги
# Предполагалось, что экземпляры класса Book будут иметь следующее формальное строковое представление:
#
# Book('<название книги>', '<автор книги>', <год выпуска книги>)
# И следующее неформальное строковое представление:
#
# <название книги> (<автор книги>, <год выпуска книги>)
# Программист торопился и решил задачу неправильно. Исправьте приведенный ниже код и реализуйте класс Book правильно.
#
# Примечание 1. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.
#
# Примечание 2. Никаких ограничений касательно реализации класса Book нет, она может быть произвольной.

class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Book('{title}', '{author}', {year})"

    def __repr__():
        return f'{title} ({author}, {year})'


# исправленый вариант:



class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f'{self.title} ({self.author}, {self.year})'

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year})"



book = Book('Изучаем Python', 'Марк Лутц', 2021)

print(book)
print(repr(book))


book = Book('Программируем на Python', 'Майкл Доусон', 2023)

print(str(book))
print(repr(book))



