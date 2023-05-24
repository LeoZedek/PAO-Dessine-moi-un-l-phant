#!/usr/bin/env python3
"""
module proposant les fonctions permettant de passer d'une
image noir et blanc à une liste ordonnée représentant le tracé
"""

import sys
import copy
import cv2 as cv
from plantcv import plantcv as pcv
import networkx as nx
import numpy as np
from dessiner_des_elephants.logique_metier.point import Point2D

def voisins_true(image, x_coord, y_coord):
    """
    Retourne la liste des voisins étant un contour d'un pixel (x, y)

    Parameters
    ----------
    image : np.ndarray
        l'image du contour
    x_coord : int
    y_coord : int

    Returns
    -------
    list
        une liste qui contient les points voisins du point (x_coord, y_coord)

    """
    voisins = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if ((i != 0 or j != 0)
                and 0 <= x_coord + i < image.shape[0]
                and 0 <= y_coord + j < image.shape[1]
                and image[x_coord+i, y_coord+j]):
                voisins.append((x_coord + i, y_coord + j))
    return voisins

def all_voisins(image, x_coord, y_coord):
    """
    Retourne la liste des voisins d'un pixel (x, y) (contour ou pas)

    Parameters
    ----------
    image : np.ndarray
        l'image du contour
    x_coord : int
    y_coord : int

    Returns
    -------
    list
        une liste qui contient tout les points voisins du point (x_coord, y_coord)
    """
    voisins = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if ((i != 0 or j != 0)
                and 0 <= x_coord + i < image.shape[0]
                and 0 <= y_coord + j < image.shape[1]):
                voisins.append((x_coord + i, y_coord + j))
    return voisins

def parcours_recursif(image, x_coord, y_coord, liste_actuelle, autres_directions, liste_de_liste, liste_intersections):
    """
    effectue un parcours de l'image récursif et stocke chaque morceau de contour dans une liste
    
    cette fonction parcours le contour en mettant a false les point explorés, 
    lorsque l'on arrive à une jonction/intersection, l'algo liste 
    les différentes directions possibles, et explore chaque direction récursivement. 
    lorsqu'il n'y a plus de voisins, l'algo ajoute la sous liste actuelle dans liste_de_liste.

    Parameters
    ----------
    image : np.ndarray
        l'image du contour
    x_coord : int
    y_coord : int
    liste_actuelle : list<tuple<int, int>>
        la direction actuellement parcourue (entre deux intersections)
    autres_directions : list<list<tuple<int, int>>>
        les autres directions partant de la même intersection que liste_actuelle
    liste_de_liste : list<list<tuple<int, int>>>
        liste qui stocke tout les bouts de tracé
    liste_intersections : list<tuple<int, int>>
        contient tout les points d'intersections du tracé

    Returns
    -------
    liste_de_liste : list<list<tuple<int, int>>>
        liste qui stocke tout les bouts de tracé
    liste_intersections : list<tuple<int, int>>
        contient tout les points d'intersections du tracé
    """
    liste_actuelle.append((x_coord,y_coord))
    image[x_coord,y_coord] = False
    point_actuel = (x_coord,y_coord)
    voisins = voisins_true(image,x_coord,y_coord)
    if len(voisins) == 0: #plus de voisins, fin de parcours
        tout_voisins = all_voisins(image, x_coord, y_coord)
        for pt_dirs in autres_directions:
            if pt_dirs in tout_voisins:
                liste_actuelle.append(pt_dirs)
        liste_de_liste.append(liste_actuelle)
    elif len(voisins) > 1: #jonction, on explore dans chaque direction
        liste_intersections.append(point_actuel)
        directions = copy.deepcopy(voisins)
        while len(directions) > 0: #tant qu'il reste des directions à explorer
            liste_annexe = [] # la sous liste qui va stocker le parcours dans la direction choisie
            point_suivant = directions.pop(0)
            #on met toute les autres directions à False (pour ne pas explorer deux à la fois)
            for pt_autres in directions:
                image[pt_autres[0], pt_autres[1]] = False
            parcours_recursif(image,
                             point_suivant[0],
                             point_suivant[1],
                             liste_annexe,
                             directions,
                             liste_de_liste,
                             liste_intersections)
            #si dernier point de la direction explorée est dans
            #la liste des directions, on le retire (pas besoin de l'explorer, on a fait une boucle)
            if liste_annexe[-1] in directions:
                directions.remove(liste_annexe[-1])
            #on remet toutes les autres directions à True (sauf celle explorée dans cette itération)
            for pt_restant in directions:
                image[pt_restant[0], pt_restant[1]] = True
        #on stocke la liste qui a permis d'arriver à
        #l'intersection (car a la fin de l'exploration des
        #différentes directions, le point d'intersection n'a plus de voisins)
        liste_de_liste.append(liste_actuelle)
    else: #un seul voisin/direction, on continue d'explorer dans cette direction
        point_suivant = voisins[0]
        parcours_recursif(image,
                            point_suivant[0],
                            point_suivant[1],
                            liste_actuelle,
                            autres_directions,
                            liste_de_liste,
                            liste_intersections)

def bitmap_to_skeleton(nom_fichier):
    """
    permet de passer du nom de fichier de l'image au squelette de celle ci

    Parameters
    ----------
    nom_fichier : str
        le nom du fichier de l'image (avec le chemin)

    Returns
    -------
    np.ndarray
        le squelette du tracé
    """
    image_bitmap = cv.imread(nom_fichier, cv.IMREAD_GRAYSCALE)
    image_inversee = 255*(image_bitmap<50) # seuil + invert colors (shape in white)
    mask_image = image_inversee == 255
    skeleton = pcv.morphology.skeletonize(mask=mask_image)
    pruned_skeleton, _, _ = pcv.morphology.prune(
                                                        skel_img=skeleton,
                                                        size=5)
    return pruned_skeleton

def bitmap_to_list_of_lists(nom_fichier):
    """
    transforme l'image bitmap en liste de listes de coordonneés

    Parameters
    ----------
    nom_fichier : str
        le nom du fichier de l'image (avec le chemin)

    Returns
    -------
    liste_de_liste : list<list<tuple<int, int>>>
        liste qui stocke tout les bouts de tracé
    liste_intersections : list<tuple<int, int>>
        contient tout les points d'intersections du tracé
    """
    sys.setrecursionlimit(10000) #limite trop basse par defaut
    image =  bitmap_to_skeleton(nom_fichier)
    #on trouve un point sur le contour pour démarrer
    index_contour = np.where(image)
    index_point_depart = 0 #point de départ choisi sur le contour
    taille_contour = len(index_contour[0])-2
    while(len(voisins_true(image,
                      index_contour[0][index_point_depart],
                      index_contour[1][index_point_depart])) < 3 ):
        index_point_depart += 1
        if index_point_depart > taille_contour:
            break
    x_depart, y_depart = index_contour[0][index_point_depart], index_contour[1][index_point_depart]

    liste_de_liste = []
    liste_intersections = []
    parcours_recursif(image,
                    x_depart,
                    y_depart,
                    [],
                    [],
                    liste_de_liste,
                    liste_intersections)
    return liste_de_liste, liste_intersections

def listes_voisines(liste, listes, image):
    """
    renvoie les listes adjacentes a la liste actuelle
    
    une liste est adajcente a une autre si son dernier ou premier
    point est voisin du premier ou dernier de l'autre

    Parameters
    ----------
    liste : list<tuple<int, int>>
        la liste testée
    listes : list<list<tuple<int, int>>>
        les listes pouvant être voisines
    image : np.ndarray
        l'image du contour

    Returns
    -------
    list<list<tuple<int, int>>>
        les listes adjacentes
    """
    listes_vois = []
    for une_liste in listes:
        if(une_liste != liste and list(reversed(une_liste)) != liste):
            l_reverse = list(reversed(une_liste))
            if une_liste[0] in voisins_true(image, liste[-1][0], liste[-1][1]):
                listes_vois.append(une_liste)
            elif l_reverse[0] in voisins_true(image, liste[-1][0], liste[-1][1]):
                listes_vois.append(l_reverse)
    return listes_vois

def sont_voisins(pt1, pt2):
    """
    renvoie True si deux points sont voisins

    Parameters
    ----------
    pt1 : tuple<int, int>
    pt2 : tuple<int, int>

    Returns
    -------
    True si les deux points sont voisins
    """
    voisins = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                voisins.append((pt1[0] + i, pt1[1] + j))
    return pt2 in voisins

def _fusion_deux_listes(listes, liste_de_deux_listes):
    """
    cette fonction permet de fusionner deux listes en gardant l'ordre

    Parameters
    ----------
    listes : list<tuple<int, int>>
        la liste contenant la fusion
    liste_de_deux_listes : list<list<tuple<int, int>>>
        les deux listes à fusionner
    """
    for couple_liste in liste_de_deux_listes:
        buffer = []
        couple_ord = (couple_liste[0], couple_liste[1]) if len(couple_liste[0]) > len(couple_liste[1]) else (couple_liste[1], couple_liste[0])
        buffer = couple_ord[0]
        buffer += list(reversed(couple_ord[1]))
        listes.remove(couple_liste[0])
        listes.remove(couple_liste[1])
        listes.append(buffer)

def _traitement_listes_non_reliees(image, listes, pts_intersection):
    """
    cette fonction traite un bug qui apparait souvent et qui fait que
    certaines listes ne sont pas reliées à un point d'intersection

    Parameters
    ----------
    image : np.ndarray
    listes : list<list<tuple<int, int>>>
        toutes les sous listes
    pts_intersection : list<tuple<int, int>>
        liste contenant les points d'intersections
    """
    deux_listes_a_fusionner = []
    for liste in listes:
        relie = False
        #si dernier pt pas intersec ou pas voisin intersec
        if liste[-1] in pts_intersection:
            relie = True
        for point in pts_intersection:
            if point in voisins_true(image, liste[-1][0], liste[-1][1]):
                relie = True
        if not relie:
           #chercher liste adj
            for liste_adj in listes:
                if((liste_adj != liste) and
                  liste_adj[-1] in voisins_true(image, liste[-1][0], liste[-1][1])):
                    lesdeux = (liste, liste_adj)
                    if (liste_adj, liste) not in deux_listes_a_fusionner:
                        deux_listes_a_fusionner.append(lesdeux)
    _fusion_deux_listes(listes, deux_listes_a_fusionner)
    #on remove les listes de 1
    for une_liste in listes:
        if len(une_liste) == 1:
            listes.remove(une_liste)

def traitement_listes_avant(image, listes, pts_intersection):
    """
    dans cette fonction, on traite le problème des listes non reliées à un point d'intersection, 
    on élimine les listes d'un seul point, et on rajoute aux listes les points d'intersections
    cette fonction doit être exécutée avant l'algorithme de postier chinois

    Parameters
    ----------
    image : np.ndarray
    listes : list<list<tuple<int, int>>>
        toutes les sous listes
    pts_intersection : list<tuple<int, int>>
        liste contenant les points d'intersections

    Returns
    -------
    list<list<tuple<int, int>>>
        toutes les sous listes traitées
    """
    _traitement_listes_non_reliees(image, listes, pts_intersection)
    listes_finales = []
    for liste in listes:
        #si premier pt pas intersect, on le cherche
        if liste[0] not in pts_intersection:
            for point in pts_intersection:
                if point in all_voisins(image, liste[0][0], liste[0][1]):
                    liste.insert(0, point)
                    break
        #pour les dead end, on sait que le premier pt est une intersec
        dead_end = True
        if liste[-1] not in pts_intersection:
            for point in pts_intersection:
                if point in all_voisins(image, liste[-1][0], liste[-1][1]):
                    liste.append(point)
                    dead_end = False
                    break
        else:
            dead_end = False
        if dead_end:
            #on est sur que c'est une dead end ici
            liste_rev = list(reversed(liste))
            liste.pop(-1)
            liste += liste_rev
        #remove les liste un seul pt intersec
        if not(len(liste) == 1 and liste[0] in pts_intersection):
            listes_finales.append(liste)
    return listes_finales

def _reconstitution_chemin(graphe_euler, chemin_postier):
    """
    cette fonction va utiliser le résultat de la méthode eulerian_circuit
    et reconstituer le chemin emprunté par cet algorithme

    Parameters
    ----------
    graphe_euler : nx.MultiGraph
        un multigraphe eulérisé
    chemin_postier : list
        l'output de la méthode eulerian_circuit

    returns
    -------
    list<tuple<int, int>>
        le chemin ordonnée permettant de reconstituer le tracé
    """
    chemin_final = []
    for edge in chemin_postier:
        depart, arrivee, index_edge = edge
        etiquette = graphe_euler[depart][arrivee][index_edge]
        liste_a_ajouter = []
        if len(etiquette) == 0:
            liste_a_ajouter = list(copy.deepcopy(graphe_euler[depart][arrivee][0]['liste']))
        else:
            liste_a_ajouter = list(copy.deepcopy(etiquette['liste']))
        #on met la liste dans le bon ordre
        if liste_a_ajouter[0] != depart:
            liste_a_ajouter = list(reversed(liste_a_ajouter))
        liste_a_ajouter.pop(-1)
        chemin_final.append(liste_a_ajouter)
    chemin_final_unpack = []
    for une_liste in chemin_final:
        for un_point in une_liste:
            chemin_final_unpack.append(un_point)
    chemin_final_unpack.append(chemin_postier[-1][1])
    return chemin_final_unpack

def postier_chinois(listes, pts_intersection):
    """
    Cette fonction construit un graphe avec les intersections comme noeuds et les bouts de
    dessin comme arêtes, et on utilise ensuite l'algorithme du postier chinois afin de trouver
    le tracé du dessin

    Parameters
    ----------
    listes : list<list<tuple<int, int>>>
        toutes les sous listes traitées
    pts_intersection : list<tuple<int, int>>
        liste contenant les points d'intersections

    Returns
    -------
    list<tuple<int, int>>
        le chemin ordonnée permettant de reconstituer le tracé
    """
    graphe = nx.MultiGraph()
    graphe.add_nodes_from(pts_intersection)
    for liste in listes:
        graphe.add_edges_from([(liste[0], liste[-1], {'liste' : liste})])
    #ajout edge si deux pts intersections voisins
    for point in pts_intersection:
        for pt_possible in pts_intersection:
            if point != pt_possible and sont_voisins(point, pt_possible):
                print(point, pt_possible)
                liste_courte = [point, pt_possible]
                graphe.add_edges_from([(point, pt_possible, {'liste' : liste_courte})])
    graphe_euler = nx.eulerize(graphe)
    chemin_postier = list(nx.eulerian_circuit(graphe_euler, keys=True))
    return _reconstitution_chemin(graphe_euler, chemin_postier)

def _inverser_trace(trace, dim_v):
    """
    permet d'inverser les dimensions ainsi que les points selon
    un axe de symétrie horizontal (pour que la liste marche dans le programme)

    Parameters
    ----------
    trace : list<tuple<int, int>>
    dim_v : int
        la dimension verticale du screen

    Returns
    -------
    list<tuple<int, int>>
        la liste avec les bonnes valeurs de points
    """
    trace_final = []
    axe = dim_v // 2
    for point in trace:
        nv_pt = point
        if point[0] < axe:
            nv_pt = (point[0] + 2*(axe - point[0]), point[1])
        elif point[0] > axe:
            nv_pt = (point[0] - 2*(point[0] - axe), point[1])
        trace_final.append(nv_pt)
    return trace_final

def image_to_list_points(filename, screen):
    """
    cette fonction permet de passer d'une image (sous forme d'un
    nom de fichier) à une liste de points ordonnée en utilisant les 
    fonctions ci-dessus

    Parameters
    ----------
    filename : str
        le nom du fichier de l'image (avec le chemin)
    screen : pg.surface.Surface
        la surface d'affichage pygame

    Returns
    -------
    list<Point2D>
        la liste ordonnée du contour dans un format utilisable par le programme
    """
    x_dimension, y_dimension = screen.get_size()
    liste_de_liste, liste_intersections = bitmap_to_list_of_lists(filename)
    image_small = bitmap_to_skeleton(filename)
    dim_v, _ = image_small.shape
    liste_de_liste_graphe = traitement_listes_avant(image_small,
                                                    liste_de_liste,
                                                    liste_intersections)
    trace = postier_chinois(liste_de_liste_graphe, liste_intersections)
    trace_final = _inverser_trace(trace, dim_v)
    liste = list(map(lambda x: Point2D(
                        float(x[1] - (x_dimension//2)),
                        float(x[0] - (y_dimension//2))),
                        trace_final))
    liste.append(liste[0])
    return liste
