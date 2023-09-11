"""
Make a list of geometrical shapes and order them by area.

>>> c = Circle(1)
>>> t = Triangle(0, 4, 3j)
>>> q = Quadrilateral(0, 2, 2+2.5j, 2.5j)
>>> sorted([c, t, q])
[Circle of area 3.14, Quadrilateral of area 5.00, Triangle of area 6.00]
"""

import doctest
import math


class Shape(object):
    def __lt__(self, shape):
        return self.area() < shape.area()

    def __repr__(self):
        return f"{type(self).__name__} of area {self.area():.2f}"


class Circle(Shape):
    """Define a circle by its radius.

    >>> c = Circle(2)
    >>> c.area()/math.pi
    4.0
    """

    def __init__(self, radius):
        assert radius > 0, "Only positive radius"
        self.r = radius

    def area(self):
        # not very spectacular
        return math.pi * self.r ** 2


class Triangle(Shape):
    """Define a triangle by three vertices.

    >>> t = Triangle(0, 4, 3j)
    >>> t.area()
    6.0
    """

    def __init__(self, a, b, c):
        self.v1 = b - a
        self.v2 = c - a

    def area(self):
        # z1.conjugate() * z2 = dot(z1, z2) + cross(z1, z2) * j
        # area is half of the abs value of the cross product
        return abs((self.v1.conjugate() * self.v2).imag) / 2.0


class Quadrilateral(Shape):
    """Define a quadrilateral by four vertices.

    >>> q = Quadrilateral(0, 2, 2+2.5j, 2.5j)
    >>> q.area()
    5.0
    """

    def __init__(self, a, b, c, d):
        # cut the quadrilateral into two triangles and sum the areas
        self.t1 = Triangle(a, b, c)
        self.t2 = Triangle(c, d, a)

    def area(self):
        return self.t1.area() + self.t2.area()


if __name__ == "__main__":

    print(doctest.testmod())
