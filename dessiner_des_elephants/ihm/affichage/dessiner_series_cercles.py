#!/usr/bin/env python3
""" definition des fonction pour dessiner les séries de cercles """

import numpy as np
import pygame as pg
from ...logique_metier.series_cercles import SeriesCercles
from ...logique_metier.point import Point2D

BLACK = 0, 0, 0
WHITE = 255, 255, 255

TAILLE_POINT = 2


def __polaire2carthesien(rho, phi):
    """
    number * number -> number, number
    rho : number la distance à zero à l'origine
    phi : l'angle du point
    return : les coordonnées carthésienne abscisse et ordonnee
    """
    abscisse = rho*np.cos(phi)
    # Because the y axes from pygame is heading down
    ordonnee = -rho*np.sin(phi)
    return abscisse, ordonnee


def __avancement_cercle(angle, pas):
    """
    number*number  -> number
    angle : number l'angle compris entre 0 et 2pi
    pas :number  le pas d'avancement du cercle
    return : number le nouvel angle
    """
    if angle < 2*np.pi:
        res = pas+angle
    elif angle >= 2*np.pi:
        res = 0
    else:
        res = 0  # pas possible faire une erreur
    return res


def __dessiner_le_chemin(series_cercles: SeriesCercles, screen):
    """
    dessine le chemin parcouru
    """
    for point in series_cercles.chemin:
        if point:
            pg.draw.circle(surface=screen, color=BLACK,
                           center=(point.abscisse, point.ordonnee), radius=TAILLE_POINT)

# Utiliser la classe coordonnée 2D


def __dessiner_cercle_et_point(ecran, abscisse, ordonnee, rayon):
    """
    ecran : la surface pygame sur laquelle on dessine
    abscisse,ordonnee : les coordonées 2D carthésienne du centre du cercle
    rayon : le rayon du grand cercle
    """
    # Transformer en constante dans le fichier
    pg.draw.circle(surface=ecran, color=BLACK, center=(
        abscisse, ordonnee), radius=TAILLE_POINT)
    pg.draw.circle(surface=ecran, color=BLACK, center=(
        abscisse, ordonnee), radius=rayon, width=1)


def __dessiner_les_cercles(series_cercles: SeriesCercles, screen):
    """
    dessine les cercles dans leurs Etat actuel et fait avancer les angles
    """
    abscisse = series_cercles.centre_initial.abscisse
    ordonnee = series_cercles.centre_initial.ordonnee
    __dessiner_cercle_et_point(ecran=screen, abscisse=abscisse,
                               ordonnee=ordonnee, rayon=series_cercles.liste_rayon[0])
    taille_liste = len(series_cercles.liste_rayon)
    for i in range(1, taille_liste):
        newx, newy = __polaire2carthesien(
            rho=series_cercles.liste_rayon[i-1], phi=series_cercles.angles[i])
        abscisse += newx
        ordonnee += newy
        if i == taille_liste-1:
            if (series_cercles.compteur_chemin >= series_cercles.nombre_point_chemin):
                series_cercles.compteur_chemin = 0
                series_cercles._angles = series_cercles.angles_initiales.copy()
            series_cercles.chemin[series_cercles.compteur_chemin] = Point2D(
                abscisse, ordonnee)
            series_cercles.compteur_chemin += 1

        __dessiner_cercle_et_point(ecran=screen, abscisse=abscisse,
                                   ordonnee=ordonnee, rayon=series_cercles.liste_rayon[i])
        series_cercles.angles[i] = __avancement_cercle(
            angle=series_cercles.angles[i], pas=series_cercles.liste_pas[i])


def dessiner_series_cercles(series_cercles: SeriesCercles, screen):
    __dessiner_le_chemin(series_cercles=series_cercles, screen=screen)
    __dessiner_les_cercles(series_cercles=series_cercles, screen=screen)
