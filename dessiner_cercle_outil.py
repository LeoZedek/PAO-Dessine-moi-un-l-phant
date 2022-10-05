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
    return : la liste d'avancement des cercle et la liste initiale des etat des angles
    """
    liste_pas = [i*pas for i in range(1, nb_cercle+1)]
    return liste_pas

def creation_liste_angle(coefficients):
    """ creer la liste des angles """
    liste_angle = [phase(coeff) for coeff in coefficients]
    liste_angle.append(0)

    # liste_angle = [0*i for i in range(len(coefficients)+1)]
    return liste_angle

def polaire2carthesien(rho,phi):
    """
    number * number -> number, number
    rho : number la distance à zero à l'origine
    phi : l'angle du point
    return : les coordonnées carthésienne abscisse et ordonnee
    """
    abscisse = rho*np.cos(phi)
    ordonnee = rho*np.sin(phi)
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
    nb_cercle = len(liste_coeff)//2

    liste_rayon = [np.abs(liste_coeff[nb_cercle])*scale]
    for i in range(1,nb_cercle):
        liste_rayon.append(2*scale*np.abs(liste_coeff[nb_cercle+i]))

    # liste_rayon = [np.abs(coeff)*(scale) for coeff in liste_coeff]
    liste_rayon.append(1)
    # liste_rayon = [np.abs(coeff)*(scale) for coeff in liste_coeff]
    print(liste_rayon)
    return liste_rayon
