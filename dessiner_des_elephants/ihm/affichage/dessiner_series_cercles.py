#!/usr/bin/env python3
""" definition des fonction pour dessiner les séries de cercles """
import pygame as pg
from ...logique_metier.series_cercles import SeriesCercles
from ...logique_metier.point import Point2D
from ...logique_metier.dessiner_cercle_outil import *

def __dessiner_le_chemin(series_cercles: SeriesCercles, screen):
    """
    dessine le chemin parcouru
    """
    for point in series_cercles.chemin:
        if point:
            pg.draw.circle(surface=screen, color=BLACK,
                           center=(point.abscisse, point.ordonnee), radius=TAILLE_POINT)


def __dessiner_les_cercles(series_cercles:SeriesCercles,screen):
    """
    dessine les cercles dans leurs Etat actuel et fait avancer les angles
    """
    abscisse = series_cercles.centre_initial.abscisse
    ordonnee = series_cercles.centre_initial.ordonnee
    dessiner_cercle_et_point(ecran=screen, abscisse=abscisse,
                             ordonnee=ordonnee, rayon=series_cercles.liste_rayon[0])
    taille_liste = len(series_cercles.liste_rayon)
    for i in range(1, taille_liste):
        newx, newy = polaire2carthesien(
            rho=series_cercles.liste_rayon[i-1], phi=series_cercles.angles[i])
        abscisse += newx
        ordonnee += newy
        if i == taille_liste-1:
            if (series_cercles.compteur_chemin >= series_cercles.nombre_point_chemin):
                series_cercles.compteur_chemin = 0
                series_cercles._angles = series_cercles.angles_initiales.copy()
            series_cercles.chemin[series_cercles.compteur_chemin] = Point2D(abscisse, ordonnee)
            series_cercles.compteur_chemin += 1

        dessiner_cercle_et_point(ecran=screen, abscisse=abscisse,
                                 ordonnee=ordonnee, rayon=series_cercles.liste_rayon[i])
        series_cercles.angles[i] = avancement_cercle(
            angle=series_cercles.angles[i], pas=series_cercles.liste_pas[i])


def dessiner_series_cercles(series_cercles: SeriesCercles,screen):
    __dessiner_le_chemin(series_cercles=series_cercles,screen=screen)
    __dessiner_les_cercles(series_cercles=series_cercles,screen=screen)
