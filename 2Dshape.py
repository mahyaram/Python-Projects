from abc import ABC, abstractmethod
import math


# abstract
class TwoDShape(ABC):

    def getArea(self):
        pass

    def getCircumference(self):
        pass


# children
class Square(TwoDShape):

    def __init__(self, width):
        self.width = width

    def getArea(self):
        return math.pow(self.width, 2)

    def getCircumference(self):
        return 4 * self.width


class Rectangle(TwoDShape):

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getCircumference(self):
        return 2 * self.width + 2 * self.height


class Triangle(TwoDShape):

    def __init__(self, base, height, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.base = base
        self.height = height

    def getArea(self):
        return self.base * self.height / 2

    def getCircumference(self):
        return self.a + self.b + self.c


class Paralellogram(TwoDShape):

    def __init__(self, base, height, side):
        self.base = base
        self.height = height
        self.side = side

    def getArea(self):
        return self.base * self.height

    def getCircumference(self):
        return 2 * self.base + 2 * self.side


class Circle(TwoDShape):

    # constructor
    def __init__(self, radius):
        self.radius = radius

    def getCircumference(self):
        return math.pi * 2 * self.radius

    def getArea(self):
        return math.pi * math.pow(self.radius, 2)


# drivers
shapeList = [
    Square(3),
    Rectangle(3, 10),
    Triangle(3, 10, 5, 6, 7),
    Paralellogram(3, 10, 9),
    Circle(10)
]

for shape in shapeList:
    print("Shape: " + str(shape.__class__.__name__))
    print("Area: " + str(shape.getArea()))
    print("Circumference: " + str(shape.getCircumference()))
    print()
