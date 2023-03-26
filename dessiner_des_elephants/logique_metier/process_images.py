#!/usr/bin/env python3

import numpy as np
from numpy import arange, linspace
import cv2 as cv
import pygame as pg

from dessiner_des_elephants.logique_metier.point import Point2D
from dessiner_des_elephants.ihm.affichage.draw_elephant_utils import DISTANCE_BETWEEN_POINT

def open_bitmap_image(filename):
    """
    fonction pour ouvir une image 
    
    filename : chemin vers fichier depuis racine

    return: l'image sous forme de numpy array
    """
    image = np.array(cv.imread(filename, cv.IMREAD_GRAYSCALE))
    return image

def _odd_line_number(direction):
    """
    Cette fonction prend une liste binaire en entrée et compte le nombre de successions de 0 dans la liste.
    
    direction: une liste de 0 et 255
    
    Return:
    int: le nombre de successions de 0 dans la liste
    
    """
    
    number_line = 0  
    in_line = False 
    
    for i in direction:
        if i == 0:
            if not in_line:
                in_line = True
                number_line += 1
        else:
            in_line = False
            
    return number_line % 2 == 1

def _pixel_in_shape(image, i, j):
    """
    vérifie si un pixel de coordonnées i et j est danss la forme fermée

    image : numpy array d'une image noire et blanche
    i, j : coordonnées du pixel

    return : True si le pixel est dans la forme
             False sinon
    """
    if(image[i,j] == 255):
        vertical_dim, horizontal_dim = image.shape
        up_direction = reversed(image[0:i, j])
        down_direction = image[i+1:vertical_dim, j]
        left_direction = reversed(image[i, 0:j])
        right_direction = image[i, j+1:horizontal_dim]
        return _odd_line_number(up_direction) and \
            _odd_line_number(down_direction) and \
            _odd_line_number(left_direction) and \
            _odd_line_number(right_direction)
    return False


def _cut_edge(image):
    """
    cette fonction permet de couper le contour de la forme fermée pour
    que le parcours en largeur puisse fonctionner

    image : numpy array d'une image noire et blanche

    return : le point duquel commencer le bfs
    """

    dim_v, dim_h = image.shape
    index_contour = np.where(image == 0)
    x_depart, y_depart = index_contour[0][0], index_contour[1][0]

    points_a_tester = []
    taille_voisinage = 50
    for i in range(
            max(0, x_depart - taille_voisinage), 
            min(x_depart + taille_voisinage, dim_v)):
        for j in range(
                max(0, y_depart-taille_voisinage),
                min(y_depart + taille_voisinage, dim_h)):
                if(_pixel_in_shape(image, i, j)):
                    point_in = (i, j)
                    break
                    
    up_direction = reversed(image[0:point_in[0], point_in[1]])

    #liste pour correspondance entre up_dir et coord de l'image
    link_direction_image = list(reversed([k for k in range(0, point_in[0])]))
    #couper la direction et garder dernier point
    in_line = False 
    index_entree = 0
    for index, i in enumerate(up_direction):
        if i == 255 and in_line:
            break
        if i == 0:
            if not in_line:
                in_line = True
            index_entree = index 
            image[link_direction_image[index], j] = 255

    #a partie de l'index, retrouver coord dans l image
    point_entree = (link_direction_image[index_entree], j)

    # Determine the values in the neighborhood of the point
    row, col = point_entree[0], point_entree[1]
    neighborhood = []
    coord_list = []
    for i in range(max(0, row-1), min(row+2, dim_v)):
        for j in range(max(0, col-1), min(col+2, dim_h)):
            neighborhood.append(image[i][j])
            coord_list.append((i, j))

    # Find the first 0 in the neighborhood and set all other values to 0
    found_zero = False
    point_final = (0, 0)
    for i in range(len(neighborhood)):
        if neighborhood[i] == 0:
            found_zero = True
            point_final = coord_list[i]
            continue
        if found_zero:
            neighborhood[i] = 255

    # Update the matrix with the modified neighborhood
    index = 0
    for i in range(max(0, row-1), min(row+2, dim_v)):
        for j in range(max(0, col-1), min(col+2, dim_h)):
            image[i][j] = neighborhood[index]
            index += 1
           
    return point_final

def _fix_point_image(points, screen):
    """
        Fonction qui permet d'ajouter
        des points entre le dernier Point2D de la liste et l'avant dernier
        si ces deux points sont eloigné de plus de DISTANCE_BETWEEN_POINT.

        points : la liste de Point2D
        screen : la Surface sur laquelle les points sont déssiner
    """

    x_dimension, y_dimension = screen.get_size()

    if len(points) > 1:

        point1 = points[len(points) - 2]
        point2 = points[len(points) - 1]

        distance = point1.distance(point2)
        nb_points = distance // DISTANCE_BETWEEN_POINT

        if nb_points > 0:

            if point1.abscisse == point2.abscisse:

                y_step = distance / nb_points

                if point1.ordonnee > point2.ordonnee:
                    y_step = -y_step

                # Not taking the first point because he is already in the points list.
                index = 0
                for new_y in arange(point1.ordonnee, point2.ordonnee, y_step):
                    if index > 0:
                        points.insert(len(points) - 1,
                                      Point2D(point1.abscisse, new_y))
                    index += 1


            else:
                coeff_a, coeff_b = point1.linear_equation(point2)

                x_step = (point2.abscisse - point1.abscisse) / nb_points

                index = 0
                for new_x in arange(point1.abscisse, point2.abscisse, x_step):
                    if index > 0:
                        new_y = coeff_a * new_x + coeff_b
                        points.insert(len(points) - 1, Point2D(new_x, new_y))
                    index += 1


def _list_neighbour(image, point_depart):
    """
    permet de liste les voisins d'un point de l'image
 
    image : numpy array d'une image noire et blanche
    point_depart : coordonnées du point à traiter

    return : liste des voisins du point
    """
    liste = []
    for i in range(point_depart[0]-1, point_depart[0]+2):
        for j in range(point_depart[1]-1, point_depart[1]+2):
            if(image[i,j] == 0):
                liste.append((i,j))
    return liste

def _bfs(visited, image, point_depart):
    """
    réalise un parcours en largeur du contour de la forme
    et liste les points visités dans a liste visited

    visited : liste des points du contour dans l'ordre
    image : numpy array d'une image noire et blanche
    point_depart : coordonnées desquels commencer l'algo
    """
    queue = []
    visited.append(point_depart)
    queue.append(point_depart)
    image[point_depart[0], point_depart[1]] = 255
    
    while(queue):
        m = queue.pop(0)
        for neighbour in _list_neighbour(image, m):
            image[neighbour[0], neighbour[1]] = 255
            visited.append(neighbour)
            queue.append(neighbour)

def bitmap_to_points(image, screen):
    """
    transforme une image noir et blanc en liste ordonnées de points

    image : numpy array d'une image noire et blanche
    screen : surface de l'écran

    return : liste ordonnées des points du contour
    """
    dim_v, dim_h = image.shape

    #couper la courbe pour le bfs 
    point_depart = _cut_edge(image)

    #algorithme bfs
    visited = []
    _bfs(visited, image, point_depart)
    
    #création liste Point2D
    x_dimension, y_dimension = screen.get_size()
    #reverse dessin
    visited_final = []
    axe = dim_v // 2
    for pt in visited:
        nv_pt = pt
        if pt[0] < axe:
            nv_pt = (pt[0] + 2*(axe - pt[0]), pt[1])
        elif pt[0] > axe:
            nv_pt = (pt[0] - 2*(pt[0] - axe), pt[1])
        visited_final.append(nv_pt)

    liste = list(map(lambda x: Point2D(
                        float(x[1] - (x_dimension//2)),
                        float(x[0] - (y_dimension//2))),visited_final))
    liste.append(liste[0])
    _fix_point_image(liste, screen)

    return liste
