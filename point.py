#!/usr/bin/env python3
"""Module proposant la classe Point2D"""

from math import hypot
from numpy import angle , abs

class Point2D:
    "Classe représentant un point 2D" 
    def __init__(self, x: float, y: float):
        "Méthode permettant d'initialiser un Point2D"
        self._x = x
        self._y = y
        self._module  = abs(complex(self))
        self._argument = angle(complex(self)) 

    @property
    def x(self)->float:
        return self._x

    @property
    def y(self)->float:
        return self._y
    @property 
    def module(self)->float:
        return self._module

    @property
    def argument(self)->float:
        return self._argument

    def __complex__(self):
        return complex(self.x,self.y)

    def distance(self, point2):
        if self.x == point2.x:
            return abs(self.y - point2.y)
        if self.y == point2.y:
            return abs(self.x - point2.x)
        return hypot(self.x - point2.x, self.y - point2.y)

    def linear_equation(self, point2):
        coeff_a = (point2.y - self.y) / (point2.x - self.x)
        coeff_b = self.y - coeff_a * self.x
        return coeff_a, coeff_b
