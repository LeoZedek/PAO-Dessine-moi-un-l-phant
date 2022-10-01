import numpy as np
import pygame as pg

black = 0, 0, 0
white = 255,255,255

taillePoint = 2

def creationListePasEtListeAngle(nbCercle,pas):
    """
    nbCercle : int>=0 la taille des listes à renvoyer dans notre le nombre de cercle
    pas : int>=0 le pas d'avancement de l'angle
    return : la liste d'avancement des cercle et la liste initiale des etat des angles
    """
    listePas = []
    angles = []
    for i in range(nbCercle):
        listePas +=[2*i*pas]
        angles +=[0]
    return listePas, angles

def polaire2carthesien(rho,phi):
    """
    number * number -> number, number 
    rho : number la distance à zero à l'origine
    phi : l'angle du point
    return : les coordonnées carthésienne x (absisse) et y (ordonnée) 
    """
    x = rho*np.cos(phi)
    y = rho*np.sin(phi)
    return x,y

def avancementCercle(angle,pas):
    """ 
    number*number  -> number
    angle : number l'angle compris entre 0 et 2pi
    pas :number  le pas d'avancement du cercle
    return : number le nouvel angle
    """
    if(angle<2*np.pi):
        res=pas+angle
    elif(angle>=2*np.pi):
        res = 0
    else:
        res = 0 # pas possible faire une erreur
    return res

# Utiliser la classe coordonnée 2D
def dessinerCercleEtPoint(ecran,x,y,rayon):
    """ 
    ecran : la surface pygame sur laquelle on dessine 
    x,y : les coordonées 2D carthésienne du centre du cercle
    rayon : le rayon du grand cercle
    """
    # Transformer en constante dans le fichier
    rayonPoint = 2
    pg.draw.circle(surface=ecran,color=black,center=(x,y),radius=rayonPoint)
    pg.draw.circle(surface=ecran,color=black,center=(x,y),radius=rayon,width=1)

def coeffToRayon(liste_coeff,scale):
    """ 
    liste_coeff : liste des coefficients de la décomposition de fourrier complexe
    scale : mise à l'échelle par rapport à la fenêtre d'affichage
    """
    # Je pense qu'il va y avoir une compréhension de liste
    liste_rayon = []
    for coeff in liste_coeff :
        liste_rayon.append(np.abs(coeff)*scale)
    return liste_rayon