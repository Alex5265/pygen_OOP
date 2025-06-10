# Класс ColoredPoint
# Реализуйте класс ColoredPoint, описывающий цветную точку на плоскости. При создании экземпляра класс должен принимать три аргумента в следующем порядке:
#
# x — координата точки по оси x
# y — координата точки по оси y
# color — цвет точки
# Класс ColoredPoint должен иметь три свойства:
#
# x — свойство, доступное только для чтения, возвращающее координату точки по оси x
# y — свойство, доступное только для чтения, возвращающее координату точки по оси y
# color — свойство, доступное только для чтения, возвращающее цвет точки
# Экземпляр класса ColoredPoint должен иметь следующее формальное строковое представление:
#
# ColoredPoint(<координата x>, <координата y>, '<цвет точки>')
# Также экземпляры класса ColoredPoint должны поддерживать между собой операции сравнения
# с помощью операторов == и !=. Две цветные точки считаются равными, если их цвета и
# координаты по обеим осям совпадают.
#
# Наконец, при передаче экземпляра класса ColoredPoint в функцию hash() должно возвращаться его хеш-значение,
# вычисленное с помощью функции hash() на основе кортежа, первым элементом которого является
# координата точки по оси x,
# вторым — координата точки по оси y, третьим — цвет точки.
#
# Примечание 1. Если объект, с которым происходит сравнение, некорректен, метод, реализующий операцию сравнения, должен вернуть константу NotImplemented.
#
# Примечание 2. Никаких ограничений касательно реализации класса ColoredPoint нет, она может быть произвольной.



class ColoredPoint:
    def __init__(self, x, y, color):
        self._x = x
        self._y = y
        self._color = color

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def color(self):
        return self._color

    def  __repr__(self):
        return f"{self.__class__.__name__}({self.x}, {self.y}, '{self.color}')"

    def __eq__(self, other):
        if isinstance(other, ColoredPoint):
            return self.x == other.x and self.y == other.y and self.color == other.color
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y, self.color))


point1 = ColoredPoint(1, 2, 'white')
point2 = ColoredPoint(1, 2, 'white')
point3 = ColoredPoint(3, 4, 'black')

print(point1 == point2)
print(hash(point1) == hash(point2))
print(point1 == point3)
print(hash(point1) == hash(point3))
print()

points = {ColoredPoint(1, 2, 'white'): 10, ColoredPoint(1, 2, 'black'): 20}

print(points)


point = ColoredPoint(1, 2, 'white')
print()

try:
    point.color = 'black'
except AttributeError as e:
    print('Error')

point = ColoredPoint(71, 42, 'Indigo')

not_supported = [6952, 208621309.925047, 'Крестик на моей груди, на него ты погляди', False,
                 {'whom': True, 'administration': 1862, 'collection': 56102.956722026},
                 (-326.5668977995, True, 'Темный, мрачный коридор, Я на цыпочках, как вор', 975006604.874278),
                 [3599, 26637.9272286489, 'JeGfEEwKXxCoxlTBTYnL', -25690105773711.2],
                 {'izPmPJcBqaYBUfrSHpin', -850300479586.218, 22.2224616976328}]

for item in not_supported:
    print(item == point)









