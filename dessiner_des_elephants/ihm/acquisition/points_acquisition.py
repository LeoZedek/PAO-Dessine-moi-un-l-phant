#!/usr/bin/env python3
"""Module proposant les fonctions pour acquérir les points dessiner par l'utilisateur"""

import sys
import pygame as pg
from numpy import arange, linspace
from ..affichage.draw_elephant_utils import DISTANCE_BETWEEN_POINT, POINT_RADIUS, COLOR_LINE
from ..affichage.draw_elephant_utils import COLOR_AXES, AXES_WIDTH
from ...logique_metier.point import Point2D
from ..affichage.screen_utils import clear_screen

# If the last two point of the points tab have a distance superior to DISTANCE_BETWEEN_POINT,
# a linear interpolation is made to add points between them.
# Private function
def _fix_point(points, screen):
    """Fonction privée"""

    x_dimension  , y_dimension   = screen.get_size()

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
                        pg.draw.circle(screen, COLOR_LINE, \
                            (point1.abscisse + (x_dimension   // 2), \
                            (-new_y + (y_dimension   // 2))), POINT_RADIUS)
                        points.insert(len(points) - 1, Point2D(point1.abscisse, new_y))
                    index += 1

                pg.display.update()


            else:
                coeff_a, coeff_b = point1.linear_equation(point2)

                x_step = (point2.abscisse - point1.abscisse) / nb_points

                index = 0
                for new_x in arange(point1.abscisse, point2.abscisse, x_step):
                    if index > 0:
                        new_y = coeff_a * new_x + coeff_b
                        pg.draw.circle(screen, COLOR_LINE, (\
                            new_x + (x_dimension   // 2), \
                            (-new_y + (y_dimension   // 2))), POINT_RADIUS)
                        points.insert(len(points) - 1, Point2D(new_x, new_y))
                    index += 1

                pg.display.update()

def get_points(screen)->list[Point2D]:
    """Retourne la liste des points dessiner par l'utilisateur.

        screen : la Surface sur laquelle l'utilisateur dessine.
    """

    clear_screen(screen)

    x_dimension  , y_dimension   = screen.get_size()

    # Draw axis
    for x_axis in range(x_dimension  ):
        pg.draw.circle(screen, COLOR_AXES, (x_axis, y_dimension   // 2), AXES_WIDTH)

    for y_axis in range(y_dimension  ):
        pg.draw.circle(screen, COLOR_AXES, (x_dimension   // 2, y_axis), AXES_WIDTH)

    pg.display.update()

    not_done = 1
    mouse_down = False
    points = []

    while not_done:

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

            elif event.type == pg.MOUSEBUTTONDOWN:
                mouse_down = True

            elif event.type == pg.MOUSEBUTTONUP:
                mouse_down = False
                if len(points) > 1:
                    not_done = False

            elif event.type == pg.MOUSEMOTION and mouse_down:
                new_point = Point2D(float(event.pos[0] - (x_dimension   // 2)), \
                    -float(event.pos[1] - (y_dimension   // 2)))
                points.append(new_point)
                pg.draw.circle(screen, COLOR_LINE, event.pos, POINT_RADIUS)

                _fix_point(points, screen)

            elif event.type == pg.KEYDOWN and event.key == pg.K_q:
                sys.exit()

        pg.display.update()

    if len(points) != 0:
        points.append(points[0])

        _fix_point(points, screen)

    clear_screen(screen)

    return points

def sampling_points(points, number_of_points):
    """Retourne une liste échantilloné des points

        points : la liste des points à échantilloner
        number_of_points : le nombre de points à échantilloner
    """

    points_length = len(points)

    if number_of_points > points_length:
        return points

    sampling = [points[round(i)] for i in \
        linspace(0, points_length, number_of_points - 1, endpoint = False)]

    if sampling:
        sampling.append(sampling[0])

    return sampling
