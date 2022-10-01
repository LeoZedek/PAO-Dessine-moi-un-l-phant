from tkinter import Scale
import pygame as pg
from drawElephantUtils import Point

from dessinerCercleOutil import *

class SeriesCercles:
    def __init__(self,centre_initial,liste_coeff,scale,screen,pas):
        """
        centreInitial: Point le centre du premier cercle
        liste_coeff : list[float] : liste des coefficient de la décomposition en série de fourrier
        scale : float : mise à l'échelle par rapport à la fenêtre d'affichage
        screen : screen : l'écran d'affichage
        pas : le pas d'avancement des cercles
        """
        self.centreInitial = centre_initial
        self.listeRayon = coeffToRayon(liste_coeff,scale)
        self.screen = screen
        self.chemin = []
        self.pas = pas
        self.listePas, self.angles = creationListePasEtListeAngle(nbCercle=len(self.listeRayon),pas=pas)

    def dessiner_le_chemin(self):
        """ 
        dessine le chemin parcouru
        """
        for point in self.chemin:
            pg.draw.circle(surface=self.screen,color=black,center=(point.getX(),point.getY()),radius=taillePoint)
        
    def dessiner_les_cercles(self):
        """
        dessine les cercles dans leurs Etat actuel et fait avancer les angles
        """
        x = self.centreInitial.getX()
        y = self.centreInitial.getY()
        dessinerCercleEtPoint(ecran=self.screen,x=x,y=y,rayon=self.listeRayon[0])

        for i in range(1,len(self.listeRayon)):
            newx, newy = polaire2carthesien(rho=self.listeRayon[i],phi=self.angles[i])
            x +=newx
            y +=newy
            if(i==len(self.listeRayon)-1):
                chemin +=[(x,y)]
            dessinerCercleEtPoint(ecran=self.screen,x=x,y=y,rayon=self.listeRayon[i])
            self.angles[i]=avancementCercle(angle=self.angles[i],pas=self.listePas[i])