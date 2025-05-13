class Cat:
    night_vision = True


cat1 = Cat()
cat2 = Cat()

# Cat.night_vision = False
cat1.night_vision = False
print(Cat.night_vision, dir(Cat))
print(Cat.__dict__)
print()
print(cat1.night_vision, cat1.__dict__)
print(cat2.night_vision, cat2.__dict__)



class Cat:
    pass


cat = Cat()

cat.name = 'Кемаль'
cat.age = 1

print(cat.__dict__)

delattr(cat, 'name')
delattr(cat, 'age')

print(cat.__dict__)


class ElectricCar:
    engine_type = 'electric motor'


car = ElectricCar()

delattr(car, 'engine_type')

print(getattr(car, 'engine_type', None))