# Реализуйте класс Rectangle, описывающий прямоугольник. При создании экземпляра класс должен принимать два аргумента в следующем порядке:
#
# length — длина прямоугольника
# width — ширина прямоугольника
# Экземпляр класса Rectangle должен иметь два атрибута:
#
# length — длина прямоугольника
# width — ширина прямоугольника
# Класс Rectangle должен иметь два свойства:
#
# perimeter — свойство, доступное только для чтения, возвращающее периметр прямоугольника
# area — свойство, доступное только для чтения, возвращающее площадь прямоугольника
# Примечание 1. При изменении сторон прямоугольника должны изменяться его периметр и площадь.
#
# Примечание 2. Дополнительная проверка данных на корректность не требуется. Гарантируется, что реализованный класс используется только с корректными данными.

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_length(self):
        return self._length

    def get_width(self):
        return self._width

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    def set_length(self, new_length):
        self._length = new_length

    def set_width(self, new_width):
        self._width = new_width

    length = property(get_length, set_length)
    width = property(get_width, set_width)
    perimeter =property(get_perimeter)
    area = property(get_area)

rectangle = Rectangle(4, 5)

rectangle.length = 2
rectangle.width = 3
print(rectangle.length)
print(rectangle.width)
print(rectangle.perimeter)
print(rectangle.area)
