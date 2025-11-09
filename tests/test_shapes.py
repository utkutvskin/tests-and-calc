# tests/test_shapes.py
import math
import pytest
from shapes.shapes import Rectangle, Cylinder, Cube, Sphere

def test_sphere_area():
    s = Sphere(5)
    assert s.calculate_area() == pytest.approx(4 * math.pi * 25, abs=1e-3)

def test_sphere_volume():
    s = Sphere(5)
    assert s.calculate_volume() == pytest.approx((4/3) * math.pi * 125, abs=1e-3)

def test_cylinder_area():
    c = Cylinder(3, 7)
    assert c.calculate_area() == pytest.approx(2 * math.pi * 3 * (3 + 7), abs=1e-3)

def test_cylinder_volume():
    c = Cylinder(3, 7)
    assert c.calculate_volume() == pytest.approx(math.pi * 9 * 7, abs=1e-3)

def test_cube_area():
    cube = Cube(4)
    assert cube.calculate_area() == pytest.approx(96, abs=1e-3)

def test_cube_volume():
    cube = Cube(4)
    assert cube.calculate_volume() == pytest.approx(64, abs=1e-3)

def test_rectangle_area():
    r = Rectangle(4, 8)
    assert r.calculate_area() == pytest.approx(32, abs=1e-12)

def test_rectangle_volume_zero():
    r = Rectangle(4, 8)
    assert r.calculate_volume() == pytest.approx(0.0, abs=1e-12)
