#!/usr/bin/env python3
""" definition de la classe SeriesCercles """
from math import pi
from .point import Point2D

from cmath import phase
import numpy as np


def _creation_liste_pas(nb_cercle: int, pas: int) -> list[float]:
    """
    nbCercle : int>=0 la taille des listes à renvoyer dans notre le nombre de cercle
    pas : int>=0 le pas d'avancement de l'angle
    return : la liste d'avancement des cercle
    """
    liste_pas = [0]
    for i in range(1, nb_cercle // 2 + 1):
        liste_pas.append(-(i) * pas)
        liste_pas.append((i) * pas)
    if nb_cercle % 2 == 1:
        liste_pas.append(-(nb_cercle // 2 + 1) * (nb_cercle // 2 + 1) * pas)
    return liste_pas


def _creation_liste_angle(coefficients: list[complex]) -> list[float]:
    """ creer la liste des angles """
    liste_angle = [0] + [phase(coefficient) for coefficient in coefficients]
    return liste_angle


def _coeff2rayon(liste_coeff: list[complex], scale: float) -> list:
    """
    liste_coeff : liste des coefficients de la décomposition de fourrier complexe
    scale : mise à l'échelle par rapport à la fenêtre d'affichage
    """
    liste_rayon = [np.abs(coefficient)*scale for coefficient in liste_coeff]
    liste_rayon.append(0)
    return liste_rayon


class SeriesCercles:
    """
    SeriesCercles permettant de dessiner les cercle
    de la décomposition en série de fourrier et de refaire le dessin
    """

    def __init__(self, centre_initial: Point2D, liste_coeff: list[complex],
                 scale: float, pas: float):
        """
        centreInitial: Point le centre du premier cercle
        liste_coeff : list[float] : liste des coefficient de la décomposition en série de fourrier
        scale : float : mise à l'échelle par rapport à la fenêtre d'affichage
        pas : le pas d'avancement des cercles
        """

        self._centre_initial = centre_initial

        self._liste_rayon = _coeff2rayon(liste_coeff, scale)
        self._pas = pas
        nombre_point_chemin = int(2*(pi//pas))
        self._chemin = [None]*nombre_point_chemin
        self._nombre_point_chemin = nombre_point_chemin
        nb_cercle = len(self.liste_rayon) - 1
        self._liste_pas = _creation_liste_pas(nb_cercle, pas)
        self._angles = _creation_liste_angle(liste_coeff)
        self._angles_initiales = self._angles.copy()
        self._compteur_chemin = 0

    @property
    def nombre_point_chemin(self):
        """ renvoi le nombre de point dans le chemin """
        return self._nombre_point_chemin

    # @nombre_point_chemin.setter
    # def nombre_point_chemin(self, nombre_point_chemin):
    #     self._nombre_point_chemin = nombre_point_chemin

    @property
    def compteur_chemin(self) -> int:
        """ renvoi la position parcouru dans le chemin """
        return self._compteur_chemin

    @compteur_chemin.setter
    def compteur_chemin(self, compteur_chemin: int):
        """Setter de l'argument compteur_chemin"""
        self._compteur_chemin = compteur_chemin

    @property
    def centre_initial(self) -> Point2D:
        """
        renvoi le centre initial
        """
        return self._centre_initial

    @property
    def liste_rayon(self) -> list[float]:
        """
        renvoi la liste des rayon
        """
        return self._liste_rayon

    @property
    def chemin(self) -> list[Point2D]:
        """
        renvoi le chemin déjà parcouru
        """
        return self._chemin

    @chemin.setter
    def chemin(self, chemin: list[Point2D]) -> None:
        """ Setter de l'arguement chemin """
        self._chemin = chemin

    @property
    def pas(self) -> float:
        """
        renvoi le pas d'avancement fixé
        """
        return self._pas

    @property
    def liste_pas(self) -> list[float]:
        """
        Renvoi la liste des pas (le pas étant différent pour chaque cercle)
        """
        return self._liste_pas

    @property
    def angles(self) -> float:
        """
        Renvoi les angles sur chaque cercle
        """
        return self._angles

    @angles.setter
    def angles(self, angles: float) -> None:
        """ Permet de set la valeur des angles """
        self._angles = angles

    @property
    def angles_initiales(self) -> float:
        """ Renvoi les phase initiale des angles """
        return self._angles_initiales

    def get_angle_first_circle(self) -> float:
        """ Retourne le premier angle """
        return self.angles[1]

    def get_initial_angle_first_circle(self) -> float:
        """ Retourne le premier angles à la position initial """
        return self._angles_initiales[1]

    def have_done_complete_tour(self) -> bool:
        """ Retourne vrai si on vient de dépasser un tour complet """
        return self.get_angle_first_circle() < self.get_initial_angle_first_circle() - 2 * pi
