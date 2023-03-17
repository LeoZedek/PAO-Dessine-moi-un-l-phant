#!/usr/bin/env python3

import numpy as np
from numpy import arange, linspace
import cv2 as cv
import pygame as pg

from dessiner_des_elephants.logique_metier.point import Point2D
from dessiner_des_elephants.ihm.affichage.draw_elephant_utils import DISTANCE_BETWEEN_POINT

def open_bitmap_image(filename):
    image = np.array(cv.imread(filename, cv.IMREAD_GRAYSCALE))
    return image

def _cut_edge(image):
    pass

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
    liste = []
    for i in range(point_depart[0]-1, point_depart[0]+2):
        for j in range(point_depart[1]-1, point_depart[1]+2):
            if(image[i,j] == 0):
                liste.append((i,j))
    return liste

def _bfs(visited, image, point_depart):
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
    #trouver un points sur la courbe
    index_contour = np.where(image == 0)
    print(index_contour)
    x_depart, y_depart = index_contour[0][0], index_contour[1][0]
    #couper la courbe pour le bfs
    #FIXME automatiser ce truc
    image[x_depart+1:x_depart+10, y_depart] = 255
    image[x_depart+1:x_depart+3, y_depart-1] = 255
    
    #algorithme bfs
    visited = []
    point_depart = (x_depart, y_depart)
    _bfs(visited, image, point_depart)
    print(len(visited))
    
    #création liste Point2D
    x_dimension, y_dimension = screen.get_size()
    liste = list(map(lambda x: Point2D(
                        float(x[1] - (x_dimension//2)),
                        float(x[0] - (y_dimension//2))),visited))
    liste.append(liste[0])
    _fix_point_image(liste, screen)

    return liste
