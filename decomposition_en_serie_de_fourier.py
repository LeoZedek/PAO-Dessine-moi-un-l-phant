#!/usr/bin/env python3
import numpy as np

def calcul_coefficient(points_complexes,nb_cercle):
    periode = 2*np.pi
    nb_point = len(points_complexes)
    pas = periode/nb_point
    temps=np.linspace(-periode/2,periode/2,nb_point)
    somme = np.trapz(points_complexes * np.exp(-1j* nb_cercle *temps * 2 * np.pi / periode),dx=pas)
    return somme/periode

def decompositions_en_serie_de_fourier(points_complexes,nb_cercle):
    return [calcul_coefficient(points_complexes,indice_coefficients)\
        for indice_coefficients in range(-nb_cercle,nb_cercle+1) ]
