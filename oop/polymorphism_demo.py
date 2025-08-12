# polymorphism_demo.py
import math

class Shape:
    """Base class representing a geometric shape"""
    def area(self):
        """Calculate area - to be overridden by subclasses"""
        raise NotImplementedError("Subclasses must implement this method")

class Rectangle(Shape):
    """Derived class representing a rectangle"""
    def __init__(self, length, width):
        """
        Initialize a rectangle
        
        :param length: Length of the rectangle
        :param width: Width of the rectangle
        """
        self.length = length
        self.width = width
    
    def area(self):
        """Calculate area of rectangle (length × width)"""
        return self.length * self.width

class Circle(Shape):
    """Derived class representing a circle"""
    def __init__(self, radius):
        """
        Initialize a circle
        
        :param radius: Radius of the circle
        """
        self.radius = radius
    
    def area(self):
        """Calculate area of circle (π × radius²)"""
        return math.pi * (self.radius ** 2)