#!/usr/bin/env python3
""" definition de la classe SeriesCercles """
import pygame as pg
from math import pi
from .dessiner_cercle_outil import creation_liste_pas
from .dessiner_cercle_outil import creation_liste_angle
from .dessiner_cercle_outil import polaire2carthesien
from .dessiner_cercle_outil import avancement_cercle
from .dessiner_cercle_outil import dessiner_cercle_et_point
from .dessiner_cercle_outil import coeff2rayon
from .dessiner_cercle_outil import BLACK, TAILLE_POINT
from .point import Point2D


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

        self._liste_rayon = coeff2rayon(liste_coeff, scale)
        self._pas = pas
        nombre_point_chemin = int(2*(pi//pas))
        self._chemin = [None]*nombre_point_chemin
        self._nombre_point_chemin = nombre_point_chemin
        nb_cercle = len(self.liste_rayon) - 1
        self._liste_pas = creation_liste_pas(nb_cercle, pas)
        self._angles = creation_liste_angle(liste_coeff)
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
    def chemin(self, chemin: list[Point2D]):
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
    def angles(self):
        """
        Renvoi les angles sur chaque cercle
        """
        return self._angles

    @angles.setter
    def angles(self, angles):
        """ Permet de set la valeur des angles """
        self._angles = angles



    @property
    def angles_initiales(self):
        """ Renvoi les phase initiale des angles """
        return self._angles_initiales

    def get_angle_first_circle(self):
        return self.angles[1]

    def get_initial_angle_first_circle(self):
        return self._angles_initiales[1]

    def have_done_complete_tour(self):
        return self.get_angle_first_circle() < self.get_initial_angle_first_circle() - 2 * pi
