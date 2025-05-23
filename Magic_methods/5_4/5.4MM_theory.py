class Angle:
    def __init__(self, value):
        self.value = value                       # градусная мера угла

    def __repr__(self):
        return f'Angle({self.value})'

    def __pos__(self):
        return Angle(self.value)

    def __neg__(self):
        return Angle(-self.value)

    def __invert__(self):
        if 0 <= self.value <= 180:
            return Angle(180 - self.value)
        return Angle(180 + self.value)


angle = Angle(100)
angle1 = Angle(-100)

print(+angle)
print(-angle)
print(~angle)
print(~angle1)
print()

import math

class Angle:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f'Angle({self.value})'

    def __abs__(self):
        return Angle(abs(self.value))

    def __round__(self, n=None):
        if n is None:
            return Angle(round(self.value))
        return Angle(round(self.value, n))

    def __trunc__(self):
        return Angle(math.trunc(self.value))

    def __floor__(self):
        return Angle(math.floor(self.value))

    def __ceil__(self):
        return Angle(math.ceil(self.value))


angle = Angle(-101.54)

print(abs(angle))
print(round(angle))
print(round(angle, 1))
print(math.trunc(angle))
print(math.floor(angle))
print(math.ceil(angle))