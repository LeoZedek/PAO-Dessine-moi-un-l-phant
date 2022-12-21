#!/usr/bin/env python3
""" Module permettant de caculer la les coefficents de la décomposition en série de Fourier """
import numpy as np


def calcul_coefficient(points_complexes, indice) -> complex:
    """ Fonction qui permet de calculer le coefficent de la\
    décomposition en série de Fourier d'indice indice"""
    periode = 2*np.pi
    nb_point = len(points_complexes)
    pas = periode/nb_point
    temps = np.linspace(-periode/2, periode/2, nb_point)
    somme = np.trapz(points_complexes * np.exp(-1j * indice *
                     temps * 2 * np.pi / periode), dx=pas)
    return somme/periode


def rangement(coefficients: list[complex], nb_cercle: int) -> list[complex]:
    """Fonction qui permet de réaranger l'ordre des coefficients

    coefficients : la liste des coefficients cn
    nb_cercles : le nombre de cercle que l'on veut créer, c'est à dire
                 le nombre de coefficients que l'on retiendra

    exemple: En entrée : [c-2, c-1, c0, c1, c2]
             En sortie : [c0, c-1, c1, c-2, c-1]
    """

    nouvelle_liste = []
    middle_ind = len(coefficients) // 2
    for i in range(1, middle_ind+1):
        nouvelle_liste.append(coefficients[middle_ind - i])
        nouvelle_liste.append(coefficients[middle_ind + i])
    if nb_cercle % 2 == 1:
        nouvelle_liste.pop()
    return nouvelle_liste


def decompositions_en_serie_de_fourier(points_complexes, nb_cercle: int) -> list[complex]:
    """ Fonction retournant l'ensemble des coefficients de l a décomposition en série de Fourier """
    borne = nb_cercle // 2
    if nb_cercle % 2 == 0:
        coefficients = [calcul_coefficient(points_complexes, indice_coefficients)
                        for indice_coefficients in range(-borne, borne+1)]
        print(len(coefficients))
    else:
        borne = borne + 1
        coefficients = [calcul_coefficient(points_complexes, indice_coefficients)
                        for indice_coefficients in range(-borne, borne+1)]
        print(len(coefficients))
    coefficients = rangement(coefficients, nb_cercle)
    return coefficients
