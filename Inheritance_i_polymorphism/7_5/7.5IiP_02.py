# Классы ChessPiece, King и Knight
# 1. Реализуйте абстрактный класс ChessPiece, описывающий шахматную фигуру. Инициализатор класса должен принимать два аргумента в следующем порядке:
#
# horizontal — координата фигуры по горизонтальной оси, представленная латинской буквой от a до h
# vertical — координата фигуры по вертикальной оси, представленная целым числом от 1 до 8 включительно
# Класс ChessPiece должен иметь один метод экземпляра:
#
# can_move() — пустой абстрактный метод
# 2. Также реализуйте класс King, наследника класса ChessPiece, описывающий шахматного короля. Процесс создания экземпляра класса King должен совпадать с процессом создания экземпляра класса ChessPiece.
#
# Класс King должен иметь один метод экземпляра:
#
# can_move() — метод, принимающий в качестве аргументов шахматные координаты по горизонтали и вертикали и возвращающий True, если фигура может переместиться по указанным координатам, или False в противном случае
# Экземпляр класса King  должен иметь два атрибута:
#
# horizontal — координата фигуры по горизонтальной оси, представленная латинской буквой от a до h
# vertical — координата фигуры по вертикальной оси, представленная целым числом от 1 до 8 включительно
# 3. Наконец, реализуйте класс Knight, наследника класса ChessPiece, описывающий шахматного коня. Процесс создания экземпляра класса Knight должен совпадать с процессом создания экземпляра класса ChessPiece.
#
# Класс Knight должен иметь один метод экземпляра:
#
# can_move() — переопределенный родительский метод, принимающий в качестве аргументов координаты по горизонтали и вертикали и возвращающий True, если фигура может переместиться по указанным координатам, и False в противном случае
# Экземпляр класса Knight  должен иметь два атрибута:
#
# horizontal — координата фигуры по горизонтальной оси, представленная латинской буквой от a до h
# vertical — координата фигуры по вертикальной оси, представленная целым числом от 1 до 8 включительно


from abc import ABC, abstractmethod


class ChessPiece(ABC):
    def __init__(self, horizontal, vertical):
        self.horizontal = horizontal
        self.vertical = vertical

    @abstractmethod
    def can_move(self, horizontal, vertical):
        pass


class King(ChessPiece):
    def can_move(self, horizontal, vertical):
        can = abs(ord(horizontal) - ord(self.horizontal)) + abs(vertical - self.vertical)
        return all(
            (
                abs(ord(horizontal) - ord(self.horizontal)) <= 1,
                abs(vertical - self.vertical) <= 1,
                can in (1, 2)
            )
        )


class Knight(ChessPiece):
    def can_move(self, horizontal, vertical):
        return (ord(self.horizontal) - ord(horizontal)) ** 2 + (self.vertical - vertical) ** 2 == 5



king = King('b', 2)

print(king.can_move('c', 3))
print(king.can_move('a', 1))
print(king.can_move('f', 7))













