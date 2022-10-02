#!/usr/bin/env python3
""" definition de la classe SeriesCercles """
# from tkinter import Scale
import pygame as pg
# from drawElephantUtils import Point

from dessiner_cercle_outil import creation_liste_pas_et_liste_angle
from dessiner_cercle_outil import polaire2carthesien
from dessiner_cercle_outil import avancement_cercle
from dessiner_cercle_outil import dessiner_cercle_et_point
from dessiner_cercle_outil import coeff2rayon
from dessiner_cercle_outil import BLACK, TAILLE_POINT
from dessiner_cercle_outil import creation_liste_angle
from point import Point2D

class SeriesCercles:
    """
    SeriesCercles permettant de dessiner les cercle
    de la décomposition en série de fourrier et de refaire le dessin
    """
    def __init__(self,centre_initial : Point2D,liste_coeff : list[complex],\
        scale : float,pas : float,screen):
        """
        centreInitial: Point le centre du premier cercle
        liste_coeff : list[float] : liste des coefficient de la décomposition en série de fourrier
        scale : float : mise à l'échelle par rapport à la fenêtre d'affichage
        screen : screen : l'écran d'affichage
        pas : le pas d'avancement des cercles
        """
        self._centre_initial = centre_initial
        self._liste_rayon = coeff2rayon(liste_coeff,scale)
        self._chemin = []
        self._pas = pas
        nb_cercle = len(self.liste_rayon)
        self._liste_pas = creation_liste_pas_et_liste_angle(nb_cercle,pas)
        self._angles = creation_liste_angle(liste_coeff)
        self._screen = screen

    @property
    def centre_initial(self)->Point2D:
        """
        renvoi le centre initial
        """
        return self._centre_initial

    @property
    def liste_rayon(self)->list[float]:
        """
        renvoi la liste des rayon
        """
        return self._liste_rayon

    @property
    def chemin(self)->list[Point2D]:
        """
        renvoi le chemin déjà parcouru
        """
        return self._chemin

    @property
    def pas(self)->float:
        """
        renvoi le pas d'avancement fixé
        """
        return self._pas

    @property
    def liste_pas(self)->list[float]:
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

    @property
    def screen(self):
        """
        renvoi l'écran sur lequel on écrit
        """
        return self._screen

    def dessiner_le_chemin(self):
        """
        dessine le chemin parcouru
        """
        for point in self.chemin:
            pg.draw.circle(surface=self.screen,color=BLACK,
                center=(point[0],point[1]),radius=TAILLE_POINT)

    def dessiner_les_cercles(self):
        """
        dessine les cercles dans leurs Etat actuel et fait avancer les angles
        """
        abscisse = self.centre_initial.x
        ordonnee = self.centre_initial.y
        dessiner_cercle_et_point(ecran=self.screen,abscisse=abscisse,\
            ordonnee=ordonnee,rayon=self.liste_rayon[0])
        taille_liste = len(self.liste_rayon)
        for i in range(1,taille_liste):
            newx, newy = polaire2carthesien(rho=self.liste_rayon[i],phi=self.angles[i])
            abscisse +=newx
            ordonnee +=newy
            if i==taille_liste-1:
                chemin = self.chemin
                chemin +=[(abscisse,ordonnee)]
            dessiner_cercle_et_point(ecran=self.screen,abscisse=abscisse,\
                ordonnee=ordonnee,rayon=self.liste_rayon[i])
            self.angles[i]=avancement_cercle(angle=self.angles[i],pas=self.liste_pas[i])
