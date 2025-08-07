class Point:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


point = Point(1, 2)

print(Point.__slots__)
print(point.__slots__)
print()



class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z


point = Point3D(1, 2, 3)

print(point.x, point.y, point.z)
print(point.__slots__)
print(point.__dict__)
print()


class Point2D:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point3D(Point2D):
    __slots__ = ('z',)

    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

point = Point3D(1, 2, 3)

print(point.x, point.y, point.z)
print(point.__slots__)
print()


from timeit import repeat

class PointWithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointWithSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y

def get_set_test(cls):
    obj = cls(0, 0)
    def get_set():
        obj.x += 1
        obj.y += 2
    return get_set


print(max(repeat(get_set_test(PointWithoutSlots))))    # результат класса без слотов
print(max(repeat(get_set_test(PointWithSlots))))       # результат класса со слотами
print()


from pympler import asizeof

class PointWithoutSlots:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class PointWithSlots:
    __slots__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


point1 = PointWithoutSlots(0, 0)
point2 = PointWithSlots(0, 0)

print(asizeof.asizeof(point1))                         # результат класса без слотов
print(asizeof.asizeof(point2))                         # результат класса со слотами



















