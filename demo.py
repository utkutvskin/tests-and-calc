# demo.py
from shapes.shapes import IShape, Sphere, Cylinder, Rectangle, Cube

def show(name: str, shape: IShape):
    print(name + ":")
    print(f"Area: {shape.calculate_area():.3f}")
    print(f"Volume: {shape.calculate_volume():.3f}")
    print()

show("Sphere",   Sphere(5))
show("Cylinder", Cylinder(3, 7))
show("Rectangle", Rectangle(4, 8))
show("Cube",     Cube(4))
