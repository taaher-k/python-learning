

#Create an abstract class Shapes with an abstract method as findarea().
#Create separate classes Circle, Square, Rectangle and implement
#findarea()



from abc import ABC, abstractmethod
import math

# Abstract Base Class
class Shapes(ABC):
    @abstractmethod
    def findarea(self):
        """Calculate area of the shape"""
        pass


# Derived Class 1: Circle
class Circle(Shapes):
    def __init__(self, radius):
        self.radius = radius

    def findarea(self):
        return math.pi * self.radius * self.radius


# Derived Class 2: Square
class Square(Shapes):
    def __init__(self, side):
        self.side = side

    def findarea(self):
        return self.side * self.side


# Derived Class 3: Rectangle
class Rectangle(Shapes):
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def findarea(self):
        return self.length * self.breadth


# --- Program Execution ---
shapes = [
    Circle(7),
    Square(5),
    Rectangle(10, 4)
]

for s in shapes:
    print(f"{s.__class__.__name__} Area: {s.findarea()}")
