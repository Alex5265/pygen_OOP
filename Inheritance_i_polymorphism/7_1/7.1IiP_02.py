# Иерархия классов 🔶
# С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов, описывающих геометрические фигуры:


class Shape:
    pass

class Circle(Shape):
    pass

class Polygon(Shape):
    pass

class Triangle(Polygon):
    pass

class IsoscelesTriangle(Triangle):
    pass

class EquilateralTriangle(Triangle):
    pass

class Quadrilateral(Polygon):
    pass

class Parallelogram(Quadrilateral):
    pass

class Rectangle(Parallelogram):
    pass

class Square(Rectangle):
    pass






print(issubclass(Circle, Shape))
print(issubclass(Polygon, Shape))
print()


print(issubclass(Triangle, Polygon))
print(issubclass(IsoscelesTriangle, Triangle))
print(issubclass(EquilateralTriangle, Triangle))















