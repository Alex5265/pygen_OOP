# Класс QuadraticPolynomial
#

class QuadraticPolynomial:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def x1(self):
        sqr = self.b ** 2 - 4 * self.a * self.c
        if sqr < 0:
            return None
        return (- self.b - sqr**0.5) / (2 * self.a)

    @property
    def x2(self):
        sqr = self.b ** 2 - 4 * self.a * self.c
        if sqr < 0:
            return None
        return ((- self.b) + sqr**0.5) / (2 * self.a)

    @property
    def view(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'.replace('+ -', '- ')

    @property
    def coefficients(self):
        return (self.a, self.b, self.c)

    @coefficients.setter
    def coefficients(self, new_coef):
        self.a, self.b, self.c = new_coef


polynom = QuadraticPolynomial(500, -601, 101)

print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)

print()

polynom.coefficients = (-1000, 1202, -202)
print(polynom.a, polynom.b, polynom.c)
print(polynom.x1)
print(polynom.x2)
print(polynom.coefficients)
print(polynom.view)



