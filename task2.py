# Продемонстрировать принцип полиморфизма через реализацию разных классов, представляющих геометрические формы,
# и метод для расчёта площади каждой формы:
# Создать базовый класс Shape с методом area(), который просто возвращает 0.
# Создать несколько производных классов для разных форм (например, Circle, Rectangle, Square), каждый из которых переопределяет метод area().
# В каждом из этих классов метод area() должен возвращать площадь соответствующей фигуры.
# Написать функцию, которая принимает объект класса Shape и выводит его площадь.

class Shape():
    def area(self):
        return 0

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, side1, side2):
        self.side1 = side1
        self.side2 = side2

    def area(self):
        return self.side1 * self.side2

class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

# circle = Circle(10)
# print(circle.area())
# rectangle = Rectangle(5,10)
# print(rectangle.area())
# square = Square(8)
# print(square.area())

def print_area(shape):
    print(f"Площадь - {shape.area()}")

circle = Circle(5)
rectangle = Rectangle(5,10)
square = Square(7)

print_area(circle)
print_area(rectangle)
print_area(square)
