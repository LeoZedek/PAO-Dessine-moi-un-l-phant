#!/usr/bin/env python3
"""Module proposant la classe Point2D"""

from math import hypot
from numpy import angle , abs

class Point2D:
    "Classe représentant un point 2D"
    def __init__(self, abscisse: float, ordonnee: float):
        "Méthode permettant d'initialiser un Point2D"
        self._abscisse = abscisse
        self._ordonnee = ordonnee
        self._module  = abs(complex(self))
        self._argument = angle(complex(self))

    @property
    def abscisse(self)->float:
        return self._abscisse

    @property
    def ordonnee(self)->float:
        return self._ordonnee
    @property
    def module(self)->float:
        return self._module

    @property
    def argument(self)->float:
        return self._argument

    def __complex__(self):
        return complex(self.abscisse,self.ordonnee)

    def distance(self, point2):
        if self.abscisse == point2.abscisse:
            return abs(self.ordonnee - point2.ordonnee)
        if self.ordonnee == point2.ordonnee:
            return abs(self.abscisse - point2.abscisse)
        return hypot(self.abscisse - point2.abscisse, self.ordonnee - point2.ordonnee)

    def linear_equation(self, point2):
        coeff_a = (point2.ordonnee - self.ordonnee) / (point2.abscisse - self.abscisse)
        coeff_b = self.ordonnee - coeff_a * self.abscisse
        return coeff_a, coeff_b
