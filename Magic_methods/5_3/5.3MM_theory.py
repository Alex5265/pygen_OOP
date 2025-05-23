class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


p1 = Point(1, 2)
p2 = Point(1, 2)
p3 = Point(3, 4)

print(p1 != p2)
print(p1 != p3)
print(p2 != p3)
print()
print(p1 == p2)
print(p1 == p3)
print(p2 == p3)
print()

p1 = Point(1, 2)

print(p1 == (1, 2))
print()

p = Point(2, 2)
points = [Point(1, 1), Point(2, 2), Point(3, 3)]

print(p in points)

print()

class First:

    def __eq__(self, other):
        return True

class Second:

    def __eq__(self, other):
        return False


print(First() == Second()) # True
print(Second() == First()) # False