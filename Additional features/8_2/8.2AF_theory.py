from enum import Enum

class Weekday(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


print(str(Weekday.MONDAY))
print(repr(Weekday.MONDAY))
print(Weekday.MONDAY.name)
print(Weekday.MONDAY.value)
print()

from enum import Enum

Weekday = Enum('Weekday', ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY'])

print(str(Weekday.MONDAY))
print(repr(Weekday.MONDAY))
print(type(Weekday.MONDAY))
print(Weekday.MONDAY.name)
print(Weekday.MONDAY.value)










