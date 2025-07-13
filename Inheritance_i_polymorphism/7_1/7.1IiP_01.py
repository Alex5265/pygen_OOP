# Иерархия классов 🛸
# С помощью наследования и приведенной ниже схемы постройте иерархию пустых классов, описывающих транспортные средства:



class Vehicle:
    pass

class LandVehicle(Vehicle):
    pass

class WaterVehicle(Vehicle):
    pass

class AirVehicle(Vehicle):
    pass

class Car(LandVehicle):
    pass

class Motorcycle(LandVehicle):
    pass

class Bicycle(LandVehicle):
    pass

class Propeller(AirVehicle):
    pass

class Jet(AirVehicle):
    pass







print(issubclass(LandVehicle, Vehicle))
print(issubclass(WaterVehicle, Vehicle))
print(issubclass(AirVehicle, Vehicle))
print()

print(issubclass(Car, LandVehicle))
print(issubclass(Motorcycle, LandVehicle))
print(issubclass(Bicycle, LandVehicle))

