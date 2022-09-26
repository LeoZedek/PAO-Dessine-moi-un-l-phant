import pygame as pg
from drawElephantUtils import Point

from dessinerCercleOutil import *

class SeriesCercles:
    def __init__(self,centreInitial,listeRayons,screen,pas):
        """
        centreInitial: Point le centre du premier cercle
        listeRayons : list[float] : liste des rayons des cercle à dessiner
        screen : screen : l'écran d'affichage
        pas : le pas d'avancement des cercles
        """
        self.centreInitial = centreInitial
        self.listeRayon = listeRayons
        self.screen = screen
        self.chemin = []
        self.pas = pas
        self.listePas, self.angles = creationListePasEtListeAngle(nbCercle=len(self.listeRayon),pas=pas)

    def dessinerLeChemin(self):
        """ 
        dessine le chemin parcouru
        """
        for point in self.chemin:
            pg.draw.circle(surface=self.screen,color=black,center=(self.centreInitial.getX(),self.centreInitial.getY()),radius=taillePoint)
        
    def dessinerLesCercles(self):
        """
        dessine les cercles dans leurs Etat actuel
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