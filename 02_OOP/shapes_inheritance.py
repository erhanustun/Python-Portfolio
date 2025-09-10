"""
shapes_inheritance.py
---------------------
Example of Inheritance and Polymorphism in Python OOP.

Concepts covered:
- Base class (Shape)
- Subclasses (Circle, Rectangle)
- Method overriding
- Polymorphism (using the same interface on different objects)
"""

import math


class Shape:
    def area(self):
        """Calculate the area of the shape (to be overridden)."""
        raise NotImplementedError("Subclasses must implement area()")

    def perimeter(self):
        """Calculate the perimeter of the shape (to be overridden)."""
        raise NotImplementedError("Subclasses must implement perimeter()")

    def __str__(self):
        """Human-readable string representation."""
        return f"{self.__class__.__name__}()"


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Area of circle: πr²"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Perimeter of circle: 2πr"""
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle(radius={self.radius})"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        """Area of rectangle: width * height"""
        return self.width * self.height

    def perimeter(self):
        """Perimeter of rectangle: 2 * (width + height)"""
        return 2 * (self.width + self.height)

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"


if __name__ == "__main__":
    # Create different shapes
    shapes = [
        Circle(5),
        Rectangle(4, 6),
        Circle(2)
    ]

    print("🔹 Polymorphism Example:")
    for shape in shapes:
        print(shape)                     # Calls __str__
        print("  Area:", shape.area())   # Same method name, different implementation
        print("  Perimeter:", shape.perimeter())
        print()
