#!/usr/bin/env python3
""" definition de la classe SeriesCercles """
import pygame as pg
from dessiner_cercle_outil import creation_liste_pas
from dessiner_cercle_outil import creation_liste_angle
from dessiner_cercle_outil import polaire2carthesien
from dessiner_cercle_outil import avancement_cercle
from dessiner_cercle_outil import dessiner_cercle_et_point
from dessiner_cercle_outil import coeff2rayon
from dessiner_cercle_outil import BLACK, TAILLE_POINT
from point import Point2D

class SeriesCercles:
    """
    SeriesCercles permettant de dessiner les cercle
    de la décomposition en série de fourrier et de refaire le dessin
    """
    def __init__(self,centre_initial : Point2D,liste_coeff : list[complex],\
        scale : float,pas : float,screen,nombre_point_chemin:int=100):
        """
        centreInitial: Point le centre du premier cercle
        liste_coeff : list[float] : liste des coefficient de la décomposition en série de fourrier
        scale : float : mise à l'échelle par rapport à la fenêtre d'affichage
        screen : screen : l'écran d'affichage
        pas : le pas d'avancement des cercles
        nombre_point_chemin : le nombre de point que l'on va garder dans le chemin
        """

        self._centre_initial = centre_initial

        self._liste_rayon = coeff2rayon(liste_coeff,scale)
        self._chemin = [None]*nombre_point_chemin
        self._nombre_point_chemin = nombre_point_chemin
        self._pas = pas
        nb_cercle = len(self.liste_rayon) - 1
        self._liste_pas = creation_liste_pas(nb_cercle,pas)
        self._angles = creation_liste_angle(liste_coeff)
        self._screen = screen
        self._compteur_chemin = 0

    @property
    def nombre_point_chemin(self):
        """ renvoi le nombre de point dans le chemin """
        return self._nombre_point_chemin
        
    @nombre_point_chemin.setter
    def nombre_point_chemin(self, nombre_point_chemin):
        self._nombre_point_chemin = nombre_point_chemin

    @property
    def compteur_chemin(self)->int:
        """ renvoi la position parcouru dans le chemin """
        return self._compteur_chemin

    @compteur_chemin.setter
    def compteur_chemin(self,compteur_chemin:int):
        """Setter de l'argument compteur_chemin"""
        self._compteur_chemin = compteur_chemin

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

    @chemin.setter
    def chemin(self,chemin:list[Point2D]):
        """ Setter de l'arguement chemin """
        self._chemin=chemin

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
            if point:
                pg.draw.circle(surface=self.screen,color=BLACK,\
                    center=(point.abscisse,point.ordonnee),radius=TAILLE_POINT)

    def dessiner_les_cercles(self):
        """
        dessine les cercles dans leurs Etat actuel et fait avancer les angles
        """
        abscisse = self.centre_initial.abscisse
        ordonnee = self.centre_initial.ordonnee
        dessiner_cercle_et_point(ecran=self.screen,abscisse=abscisse,\
            ordonnee=ordonnee,rayon=self.liste_rayon[0])
        taille_liste = len(self.liste_rayon)
        for i in range(1,taille_liste):
            newx, newy = polaire2carthesien(rho=self.liste_rayon[i-1],phi=self.angles[i])
            abscisse +=newx
            ordonnee +=newy
            if i==taille_liste-1:
                if (self.compteur_chemin >= self.nombre_point_chemin):
                    self.compteur_chemin = 0
                self.chemin[self.compteur_chemin] = Point2D(abscisse,ordonnee)
                self.compteur_chemin +=1
            dessiner_cercle_et_point(ecran=self.screen,abscisse=abscisse,\
                ordonnee=ordonnee,rayon=self.liste_rayon[i])
            self.angles[i]=avancement_cercle(angle=self.angles[i],pas=self.liste_pas[i])
