#!/usr/bin/env python3
""" definition de la classe SeriesCercles """
# from tkinter import Scale
import pygame as pg
# from drawElephantUtils import Point

from dessinerCercleOutil import creationListePasEtListeAngle
from dessinerCercleOutil import polaire2carthesien
from dessinerCercleOutil import avancementCercle
from dessinerCercleOutil import dessinerCercleEtPoint
from dessinerCercleOutil import coeffToRayon
from dessinerCercleOutil import black, taillePoint
from point import Point2D

class SeriesCercles:
    """
    SeriesCercles permettant de dessiner les cercle
    de la décomposition en série de fourrier et de refaire le dessin
    """
    def __init__(self,centre_initial : Point2D,liste_coeff : list[float],\
        scale : float,pas : float,screen):
        """
        centreInitial: Point le centre du premier cercle
        liste_coeff : list[float] : liste des coefficient de la décomposition en série de fourrier
        scale : float : mise à l'échelle par rapport à la fenêtre d'affichage
        screen : screen : l'écran d'affichage
        pas : le pas d'avancement des cercles
        """
        self._centre_initial = centre_initial
        self._liste_rayon = coeffToRayon(liste_coeff,scale)
        self._chemin = []
        self._pas = pas
        nb_cercle = len(self.liste_rayon)
        self._liste_pas, self._angles = creationListePasEtListeAngle(nbCercle=nb_cercle,pas=pas)
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
            pg.draw.circle(surface=self.screen,color=black,
                center=(point.x,point.y),radius=taillePoint)

    def dessiner_les_cercles(self):
        """
        dessine les cercles dans leurs Etat actuel et fait avancer les angles
        """
        x = self.centre_initial.getX()
        y = self.centre_initial.getY()
        dessinerCercleEtPoint(ecran=self.screen,x=x,y=y,rayon=self.liste_rayon[0])

        for i in range(1,len(self.liste_rayon)):
            newx, newy = polaire2carthesien(rho=self.liste_rayon[i],phi=self.angles[i])
            x +=newx
            y +=newy
            if i==len(self.liste_rayon)-1 :
                chemin +=[(x,y)]
            dessinerCercleEtPoint(ecran=self.screen,x=x,y=y,rayon=self.liste_rayon[i])
            self.angles[i]=avancementCercle(angle=self.angles[i],pas=self.liste_pas[i])
