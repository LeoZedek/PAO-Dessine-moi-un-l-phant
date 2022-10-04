import numpy as np
from pointsAcquisition import getPoints, samplingPoints
from screenUtils import initWindow, clearScreen
from draw_points import drawPoints
from point import Point2D

import pygame as pg

def calcul_Cn(z,nb_cercle):
    nb_point = len(z)
    pas = 2*np.pi/nb_point
    t=np.arange(-np.pi,np.pi,pas)
    somme = np.trapz(z*np.exp(-1j*nb_cercle*t),dx=pas)
    return somme/(2*np.pi), nb_cercle, t

def decompositions_en_serie_de_fourier(z,nb_cercle):
    Cn = [] 
    for nb in range(-nb_cercle ,nb_cercle + 1): 
        C_nb, nb_cercle, t = calcul_Cn(z,nb)
        Cn.append(C_nb)
    return Cn, nb_cercle, t

def signal_reconstitue(Cn, nb_cercle, t):
    T = 2 * np.pi
    z = np.zeros(len(t))
    for index, value in enumerate(Cn):
        z = z + value * np.exp(1j * (index - nb_cercle) * 2 * np.pi / T * t)

    return z

pg.init()

screen = initWindow()
xD, yD = screen.get_size()

points = getPoints(screen)
cercle = 100
points = samplingPoints(points, 1000)
pointsComplexe = [complex(point) for point in points]

print(pointsComplexe)

Cn, nb_cercle, t = decompositions_en_serie_de_fourier(pointsComplexe, cercle)

pointsReconstituer = signal_reconstitue(Cn,cercle, t)

pointsReconstituer2D = [Point2D(pointReconstituer.real, pointReconstituer.imag) for pointReconstituer in pointsReconstituer]

clearScreen(screen)

drawPoints(pointsReconstituer2D, screen, pg.Rect(0, 0, xD, yD))
input()