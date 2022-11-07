#!/usr/bin/env python3
""" definition des fonction outils pour la classe SeriesCercles """
from cmath import phase
import numpy as np
import pygame as pg

BLACK = 0, 0, 0
WHITE = 255,255,255

TAILLE_POINT = 2

def creation_liste_pas(nb_cercle,pas):
    """
    nbCercle : int>=0 la taille des listes à renvoyer dans notre le nombre de cercle
    pas : int>=0 le pas d'avancement de l'angle
    return : la liste d'avancement des cercle
    """
    liste_pas = [0]
    for i in range(1, nb_cercle // 2 + 1):
        liste_pas.append(-(i) * pas)
        liste_pas.append((i) * pas)
    if nb_cercle%2==1:
        liste_pas.append(-(nb_cercle // 2 + 1) * (nb_cercle // 2 + 1) * pas)
    return liste_pas

def creation_liste_angle(coefficients):
    """ creer la liste des angles """
    liste_angle = [0] + [phase(coefficient) for coefficient in coefficients]
    return liste_angle

def polaire2carthesien(rho,phi):
    """
    number * number -> number, number
    rho : number la distance à zero à l'origine
    phi : l'angle du point
    return : les coordonnées carthésienne abscisse et ordonnee
    """
    abscisse = rho*np.cos(phi)
    # Because the y axes from pygame is heading down
    ordonnee = -rho*np.sin(phi)
    return abscisse,ordonnee

def avancement_cercle(angle,pas):
    """
    number*number  -> number
    angle : number l'angle compris entre 0 et 2pi
    pas :number  le pas d'avancement du cercle
    return : number le nouvel angle
    """
    if angle<2*np.pi:
        res=pas+angle
    elif angle>=2*np.pi:
        res = 0
    else:
        res = 0 # pas possible faire une erreur
    return res

# Utiliser la classe coordonnée 2D
def dessiner_cercle_et_point(ecran,abscisse,ordonnee,rayon):
    """
    ecran : la surface pygame sur laquelle on dessine
    abscisse,ordonnee : les coordonées 2D carthésienne du centre du cercle
    rayon : le rayon du grand cercle
    """
    # Transformer en constante dans le fichier
    pg.draw.circle(surface=ecran,color=BLACK,center=(abscisse,ordonnee),radius=TAILLE_POINT)
    pg.draw.circle(surface=ecran,color=BLACK,center=(abscisse,ordonnee),radius=rayon,width=1)

def coeff2rayon(liste_coeff,scale):
    """
    liste_coeff : liste des coefficients de la décomposition de fourrier complexe
    scale : mise à l'échelle par rapport à la fenêtre d'affichage
    """
    liste_rayon = [np.abs(coefficient)*scale for coefficient in liste_coeff]
    liste_rayon.append(0)
    return liste_rayon
