#!/usr/bin/env python3
""" definition des fonction pour dessiner les séries de cercles """

import numpy as np
import pygame as pg
from .draw_elephant_utils import POINT_RADIUS, COLOR_LINE
from ...logique_metier.series_cercles import SeriesCercles
from ...logique_metier.point import Point2D

BLACK = 0, 0, 0
WHITE = 255, 255, 255
BLUE = 6, 28, 115
GREEN = 30, 66, 2
RED = 171, 15, 15

TAILLE_POINT = 2


def __polaire2carthesien(rho: float, phi: float) -> tuple[float, float]:
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


def __avancement_cercle(angle: float, pas: float) -> float:
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


def __dessiner_le_chemin(series_cercles: SeriesCercles, screen: pg.Surface) -> None:
    """
    dessine le chemin parcouru
    """
    #vérification des deux premiers points(affichage sous forme de droites)
    if(not(series_cercles.chemin[1])):
        if(series_cercles.chemin[0]): #si la liste ne contient qu'un seul point2D
            pg.draw.circle(surface=screen, color=BLACK,
                           center=(series_cercles.chemin[0].abscisse, series_cercles.chemin[0].ordonnee), radius=TAILLE_POINT)
    else:
        for i in range(len(series_cercles.chemin)):
            if(not(series_cercles.chemin[i+1])):
                break
            point1 = series_cercles.chemin[i]
            point2 = series_cercles.chemin[i+1]
            pg.draw.line(screen, COLOR_LINE, (point1.abscisse, point1.ordonnee),
                    (point2.abscisse, point2.ordonnee), 3)
                    

def __dessiner_cercle_et_point(ecran, abscisse: float, ordonnee: float, rayon: float) -> None:
    """
    ecran : la surface pygame sur laquelle on dessine
    abscisse,ordonnee : les coordonées 2D carthésienne du centre du cercle
    rayon : le rayon du grand cercle
    """
    # Transformer en constante dans le fichier
    pg.draw.circle(surface=ecran, color=RED, center=(
        abscisse, ordonnee), radius=TAILLE_POINT)
    pg.draw.circle(surface=ecran, color=GREEN, center=(
        abscisse, ordonnee), radius=rayon, width=2)


def __dessiner_les_cercles(series_cercles: SeriesCercles, screen: pg.Surface) -> None:
    """
    dessine les cercles dans leurs Etat actuel et fait avancer les angles
    """
    abscisse = series_cercles.centre_initial.abscisse

    ordonnee = series_cercles.centre_initial.ordonnee
    __dessiner_cercle_et_point(ecran=screen, abscisse=abscisse,
                               ordonnee=ordonnee, rayon=series_cercles.liste_rayon[0])
    newx, newy = __polaire2carthesien(
        rho=series_cercles.liste_rayon[0], phi=series_cercles.angles[1])
    abscisse2 = abscisse + newx
    ordonnee2 = ordonnee + newy

    pg.draw.line(surface=screen, color=BLUE, start_pos=(
        abscisse, ordonnee), end_pos=(abscisse2, ordonnee2), width=2)

    taille_liste = len(series_cercles.liste_rayon)
    for i in range(1, taille_liste):
        newx, newy = __polaire2carthesien(
            rho=series_cercles.liste_rayon[i-1], phi=series_cercles.angles[i])
        abscisse += newx
        ordonnee += newy

        if i != taille_liste-1:
            newx2, newy2 = __polaire2carthesien(
                rho=series_cercles.liste_rayon[i], phi=series_cercles.angles[i+1])
            abscisse2 = newx2 + abscisse
            ordonnee2 = newy2 + ordonnee
            pg.draw.line(surface=screen, color=BLUE, start_pos=(
                abscisse, ordonnee), end_pos=(abscisse2, ordonnee2), width=2)

        else:
            if series_cercles.compteur_chemin >= series_cercles.nombre_point_chemin:
                series_cercles.compteur_chemin = 0
                series_cercles.angles(
                    angles=series_cercles.angles_initiales.copy())
            series_cercles.chemin[series_cercles.compteur_chemin] = Point2D(
                abscisse, ordonnee)
            series_cercles.compteur_chemin += 1

        __dessiner_cercle_et_point(ecran=screen, abscisse=abscisse,
                                   ordonnee=ordonnee, rayon=series_cercles.liste_rayon[i])
        series_cercles.angles[i] = __avancement_cercle(
            angle=series_cercles.angles[i], pas=series_cercles.liste_pas[i])


def dessiner_series_cercles(series_cercles: SeriesCercles, screen: pg.Surface) -> None:
    """ Dessine d'abord le chemin puis al série de cercle """
    __dessiner_le_chemin(series_cercles=series_cercles, screen=screen)
    __dessiner_les_cercles(series_cercles=series_cercles, screen=screen)
