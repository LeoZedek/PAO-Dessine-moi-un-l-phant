#!/usr/bin/env python3
""" Module permettant de caculer la les coefficents de la décomposition en série de Fourier """
import numpy as np

def calcul_coefficient(points_complexes,indice)->complex:
    """ Fonction qui permet de calculer le coefficent de la\
    décomposition en série de Fourier d'indice """
    periode = 2*np.pi
    nb_point = len(points_complexes)
    pas = periode/nb_point
    temps=np.linspace(-periode/2,periode/2,nb_point)
    somme = np.trapz(points_complexes * np.exp(-1j* indice *temps * 2 * np.pi / periode),dx=pas)
    return somme/periode

def decompositions_en_serie_de_fourier(points_complexes,nb_cercle)->list[complex]:
    """ Fonction retournant l'ensemble des coefficients de l a décomposition en série de Fourier """
    return [calcul_coefficient(points_complexes,indice_coefficients)\
        for indice_coefficients in range(-nb_cercle,nb_cercle+1) ]
