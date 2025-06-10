class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y


p1 = Point(1, 2)
p2 = Point(1, 2)

print(hash(p1), id(p1) // 16)
print(hash(p2), id(p2) // 16)
print()

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(1, 2)
p2 = Point(1, 2)

print(p1 == p2)
print(hash(p1) == hash(p2))
print()


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return NotImplemented

    def __hash__(self):
        return 123456789012345678901234567890 # 123456789012345678901234567890 % 2305843009213693951


p = Point(1, 2)

print(hash(p))
print(123456789012345678901234567890 % 2305843009213693951)
print()


class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if isinstance(other, Point):
            return self._fields == other._fields
        return NotImplemented

    def __hash__(self):
        return hash(self._fields)

    @property
    def _fields(self):
        return self.x, self.y, self.z


p1 = Point(1, 2, 3)
p2 = Point(1, 2, 3)
p3 = Point(4, 5, 6)

print(p1 == p2)
print(p1 == p3)
print(hash(p1) == hash(p2))
print(hash(p1) == hash(p3))
print()

class Cat:
    def __init__(self, name):
        self.name = name

    def __eq__(self, other):
        if isinstance(other, Cat):
            return self.name == other.name
        return NotImplemented

    def __hash__(self):
        return hash(self.name)


cat1 = Cat('Кемаль')
cat2 = Cat('Кемаль')

print(cat1 == cat2)
print(hash(cat1) == hash(cat2))