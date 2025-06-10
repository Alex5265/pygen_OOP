class Angle:
    def __init__(self, value):
        self.value = value                      # градусная мера угла


print(bool(Angle(-110)))
print(bool(Angle(0)))
print(bool(Angle(0.0)))
print(bool(Angle(120.1)))
print()

class Angle:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        return self.value != 0


print(bool(Angle(-110)))
print(bool(Angle(0)))
print(bool(Angle(0.0)))
print(bool(Angle(120.1)))
print()

class Angle:
    def __init__(self, value):
        self.value = value

    def __len__(self):
        print('Вызов метода __len__()')
        return self.value != 0


print(bool(Angle(-110)))
print(bool(Angle(0)))
print(bool(Angle(120.1)))
print()

class Angle:
    def __init__(self, value):
        self.value = value

    def __bool__(self):
        print('Вызов метода __bool__()')
        return bool(self.value)


angles = [Angle(100), Angle(110), Angle(-50), Angle(0)]

print(all(angles))
print()
print(any(angles))
print()

class Angle:
    def __init__(self, value):
        self.value = value

    def __index__(self):
        print('Вызов метода __index__()')
        return self.value


angle = Angle(100)

print(int(angle))
print(float(angle))
print(bin(angle))
print(oct(angle))
print(hex(angle))

