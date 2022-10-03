#!/usr/bin/env python3
import numpy as np

def calcul_Cn(z,nb_cercle):
    nb_point = len(z)
    pas = 2*np.pi/nb_point
    t=np.linspace(-np.pi,np.pi,nb_point)
    somme = np.trapz(z*np.exp(-1j*nb_cercle*t),dx=pas)
    return somme/(2*np.pi)

def decompositions_en_serie_de_fourier(z,nb_cercle):
    Cn = []
    for nb in range(-nb_cercle ,nb_cercle + 1): 
        C_nb = calcul_Cn(z,nb)
        Cn.append(C_nb)
    return Cn
