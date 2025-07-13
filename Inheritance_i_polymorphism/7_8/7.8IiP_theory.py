class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def perimeter(self):
        return (self.length + self.width) * 2

    def area(self):
        return self.length * self.width


class Square:
    def __init__(self, side):
        self.value = Rectangle(side, side)

    def perimeter(self):
        return self.value.perimeter()

    def area(self):
        return self.value.area()


square = Square(2)

print(square.perimeter())
print(square.area())




class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay                                        # ежемесячная зарплата
        self.bonus = bonus                                    # ежегодная премия

    def annual_salary(self):
        return 12 * self.pay + self.bonus                     # годовая зарплата

class Employee:
     def __init__(self, name, pay, bonus):
         self.name = name
         self.salary = Salary(pay, bonus)                     # объект, содержащий все данные о зарплате

     def total_salary(self):
         return self.salary.annual_salary()


employee = Employee('Гвидо', 100000, 10000)

print(employee.total_salary())



