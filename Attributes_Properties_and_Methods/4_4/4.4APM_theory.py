class ElectricCar:
    def __init__(self, color):
        self.__color = color


car = ElectricCar('black')

car.__color = 'yellow'

print(car.__color)