# shapes/shapes.py
import math
from abc import ABC, abstractmethod

class IShape(ABC):
    @abstractmethod
    def calculate_area(self) -> float: ...
    @abstractmethod
    def calculate_volume(self) -> float: ...

class Rectangle(IShape):
    def __init__(self, length: float, width: float):
        self.length = float(length)
        self.width = float(width)

    def calculate_area(self) -> float:
        return self.length * self.width

    def calculate_volume(self) -> float:
        return 0.0  # 2D

class Cylinder(IShape):
    def __init__(self, radius: float, height: float):
        self.radius = float(radius)
        self.height = float(height)

    def calculate_area(self) -> float:
        return 2 * math.pi * self.radius * (self.radius + self.height)

    def calculate_volume(self) -> float:
        return math.pi * (self.radius ** 2) * self.height

class Cube(IShape):
    def __init__(self, side: float):
        self.side = float(side)

    def calculate_area(self) -> float:
        return 6 * (self.side ** 2)

    def calculate_volume(self) -> float:
        return self.side ** 3

class Sphere(IShape):
    def __init__(self, radius: float):
        self.radius = float(radius)

    def calculate_area(self) -> float:
        return 4 * math.pi * (self.radius ** 2)

    def calculate_volume(self) -> float:
        return (4.0 / 3.0) * math.pi * (self.radius ** 3)
