#!/usr/bin/env python3
"""Module proposant la classe Point2D"""

from math import hypot

class Point2D:
    """" Classe représentant un point 2D """
    def __init__(self, abscisse: float, ordonnee: float):
        "Méthode permettant d'initialiser un Point2D"
        self._abscisse = abscisse
        self._ordonnee = ordonnee

    @property
    def abscisse(self)->float:
        """ Retourne l'abscisse du point """
        return self._abscisse

    @property
    def ordonnee(self)->float:
        """ Retourne l'ordonnée du point """
        return self._ordonnee

    @abscisse.setter
    def abscisse(self, abscisse):
        self._abscisse = abscisse

    @ordonnee.setter
    def ordonnee(self,ordonnee):
        self._ordonnee = ordonnee

    def __complex__(self):
        return complex(self.abscisse,self.ordonnee)

    def distance(self, point2):
        """ Permet de calculer la distance entre 2 points

        point2 : le Point2D auquel on veux calculer la distance
         """
        if self.abscisse == point2.abscisse:
            return abs(self.ordonnee - point2.ordonnee)
        if self.ordonnee == point2.ordonnee:
            return abs(self.abscisse - point2.abscisse)
        return hypot(self.abscisse - point2.abscisse, self.ordonnee - point2.ordonnee)

    def linear_equation(self, point2):
        """ Permet d'obtenir l'équation linéaire entre 2 points

        point2 : Le deuxième Point2D pour calculer l'équation
        """
        coeff_a = (point2.ordonnee - self.ordonnee) / (point2.abscisse - self.abscisse)
        coeff_b = self.ordonnee - coeff_a * self.abscisse
        return coeff_a, coeff_b
