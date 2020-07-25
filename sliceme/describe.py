"""The following license applies to the Vector class only"""

""" 
The MIT License (MIT)
Copyright (c) 2015 Mat Leonard
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
"""

import math
import numpy as np
from sympy.core import Expr


class Vector(object):
    """
    CONSTRUCTORS
    Vector(a: symbol, b: symbol, c: symbol)
    Vector(point: str, var: dict)
    """

    def __init__(self, *args):
        """Create a vector, example: v = Vector(a, b, c)"""
        if len(args) == 3:
            # a: symbol, b: symbol, c: symbol
            self.values = args
        elif len(args) == 2:
            # point: str, var: dict
            point = args[0]
            var = args[1]
            self.values = var[point]
        else:
            raise ValueError(f'{" ".join(map(str, args))} are invalid arguments')

    def norm(self):
        """Returns the norm (length, magnitude) of the vector"""
        return sum(comp ** 2 for comp in self) ** (1 / 2)

    def argument(self):
        """Returns the argument of the vector, the angle clockwise from +y"""
        arg_in_rad = math.acos(Vector(0, 1, 0) * self / self.norm())
        arg_in_deg = math.degrees(arg_in_rad)
        if self.values[0] < 0:
            return 360 - arg_in_deg
        else:
            return arg_in_deg

    def normalize(self):
        """Returns a normalized unit vector"""
        norm = self.norm()
        normed = tuple(comp / norm for comp in self)
        return Vector(*normed)

    # def rotate(self, *args):
    #     """ Rotate this vector. If passed a number, assumes this is a
    #         2D vector and rotates by the passed value in degrees.  Otherwise,
    #         assumes the passed value is a list acting as a matrix which rotates the vector.
    #     """
    #     if len(args) == 1 and type(args[0]) == type(1) or type(args[0]) == type(1.):
    #         # So, if rotate is passed an int or a float...
    #         if len(self) != 2:
    #             raise ValueError("Rotation axis not defined for greater than 2D vector")
    #         return self._rotate2D(*args)
    #     elif len(args) == 1:
    #         matrix = args[0]
    #         if not all(len(row) == len(v) for row in matrix) or not len(matrix) == len(self):
    #             raise ValueError("Rotation matrix must be square and same dimensions as vector")
    #         return self.matrix_mult(matrix)

    # def _rotate2D(self, theta):
    #     """ Rotate this vector by theta in degrees.
    #
    #         Returns a new vector.
    #     """
    #     theta = math.radians(theta)
    #     # Just applying the 2D rotation matrix
    #     dc, ds = math.cos(theta), math.sin(theta)
    #     x, y = self.values
    #     x, y = dc * x - ds * y, ds * x + dc * y
    #     return Vector(x, y)

    # def matrix_mult(self, matrix):
    #     """ Multiply this vector by a matrix.  Assuming matrix is a list of lists.
    #
    #         Example:
    #         mat = [[1,2,3],[-1,0,1],[3,4,5]]
    #         Vector(1,2,3).matrix_mult(mat) ->  (14, 2, 26)
    #
    #     """
    #     if not all(len(row) == len(self) for row in matrix):
    #         raise ValueError('Matrix must match vector dimensions')
    #
    #         # Grab a row from the matrix, make it a Vector, take the dot product,
    #     # and store it as the first component
    #     product = tuple(Vector(*row) * self for row in matrix)
    #
    #     return Vector(*product)

    def inner(self, other):
        """Returns the dot product (inner product) of self and other vector"""
        return sum(a * b for a, b in zip(self, other))

    def cross(self, other):
        """Cross product of self and other"""
        return Vector(self[1] * other[2] - self[2] * other[1],
                      self[2] * other[0] - self[0] * other[2],
                      self[0] * other[1] - self[1] * other[0])

    def angle(self, other):
        """Angle between self and another vector"""
        return self.inner(other) / (self.norm() * other.norm())

    def __mul__(self, other):
        """ Returns the dot product of self and other if multiplied
            by another Vector.  If multiplied by an int or float,
            multiplies each component by other.
        """
        if isinstance(other, Vector):
            return self.inner(other)
        elif isinstance(other, int) or isinstance(other, float) or isinstance(other, Expr):
            product = tuple(a * other for a in self)
            return Vector(*product)
        else:
            raise TypeError(f'Cannot multiply Vector by {type(other)}')

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if type(other) == type(1) or type(other) == type(1.0):
            divided = tuple(a / other for a in self)
            return Vector(*divided)

    def __add__(self, other):
        """ Returns the vector addition of self and other """
        added = tuple(a + b for a, b in zip(self, other))
        return Vector(*added)

    def __sub__(self, other):
        """ Returns the vector difference of self and other """
        subbed = tuple(a - b for a, b in zip(self, other))
        return Vector(*subbed)

    def __iter__(self):
        return self.values.__iter__()

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def __repr__(self):
        return str(self.values)


def angle(a, b, c, d, var):
    # todo
    return ''


def point_distance(a: str, b: str, var: dict):
    """Distance between points A and B"""
    return (Vector(a, var) - Vector(b, var)).norm()


def perpendicular(a, b, c, d, var):
    """AB being perpendicular to CD"""
    return (Vector(b, var) - Vector(a, var)) * (Vector(d, var) - Vector(c, var))


def parallel(a, b, c, d, var):
    """AB being parallel to CD"""
    return (Vector(b, var) - Vector(a, var)).cross(Vector(d, var) - Vector(c, var)).norm()


def equate(a, b):
    return a - b
