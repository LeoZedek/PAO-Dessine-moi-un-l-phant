#!/usr/bin/env python3
"""Module proposant les fonctions pour acquérir les points dessiner par l'utilisateur"""

import sys
import pickle
import pygame as pg
from numpy import arange, linspace
from dessiner_des_elephants.traduction import _

from dessiner_des_elephants.ihm.affichage.drawing_rectangle import DrawingRectangle
from ..affichage.draw_elephant_utils import DISTANCE_BETWEEN_POINT, POINT_RADIUS, COLOR_LINE
from ..affichage.draw_elephant_utils import COLOR_AXES, AXES_WIDTH
from ...logique_metier.point import Point2D
from ..affichage.screen_utils import clear_screen
from ..affichage.text_box import TextBox

from dessiner_des_elephants.logique_metier.process_images import bitmap_to_points, open_bitmap_image


# If the last two point of the points tab have a distance superior to DISTANCE_BETWEEN_POINT,
# a linear interpolation is made to add points between them.
# Private function


def _fix_point(points, screen):
    """
        Fonction qui permet d'ajouter et de dessiner (grace à une interpolation linéaire)
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
                        pg.draw.circle(screen, COLOR_LINE,
                                       (point1.abscisse + (x_dimension // 2),
                                        (-new_y + (y_dimension // 2))), POINT_RADIUS)
                        points.insert(len(points) - 1,
                                      Point2D(point1.abscisse, new_y))
                    index += 1

                pg.display.update()

            else:
                coeff_a, coeff_b = point1.linear_equation(point2)

                x_step = (point2.abscisse - point1.abscisse) / nb_points

                index = 0
                for new_x in arange(point1.abscisse, point2.abscisse, x_step):
                    if index > 0:
                        new_y = coeff_a * new_x + coeff_b
                        pg.draw.circle(screen, COLOR_LINE, (
                            new_x + (x_dimension // 2),
                            (-new_y + (y_dimension // 2))), POINT_RADIUS)
                        points.insert(len(points) - 1, Point2D(new_x, new_y))
                    index += 1

                pg.display.update()


def _get_points_manually(screen) -> list[Point2D]:
    """Retourne la liste des points dessiner par l'utilisateur.

        screen : la Surface sur laquelle l'utilisateur dessine

        return : la liste des Point2D que l'utilisateur à dessiné
    """

    clear_screen(screen)

    x_dimension, y_dimension = screen.get_size()

    # Draw axis
    for x_axis in range(x_dimension):
        pg.draw.circle(screen, COLOR_AXES,
                       (x_axis, y_dimension // 2), AXES_WIDTH)

    for y_axis in range(y_dimension):
        pg.draw.circle(screen, COLOR_AXES,
                       (x_dimension // 2, y_axis), AXES_WIDTH)

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
                new_point = Point2D(float(event.pos[0] - (x_dimension // 2)),
                                    -float(event.pos[1] - (y_dimension // 2)))
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


def _affichage_image(screen, nom_fichier, left, top, width, height, x_dimension, y_dimension):

    with open(nom_fichier, "rb") as file:
        new_points, x_dimension_charge, y_dimension_charge = pickle.load(file)

    x_ratio = x_dimension / x_dimension_charge
    y_ratio = y_dimension / y_dimension_charge

    for point in new_points:
        point.abscisse = point.abscisse*x_ratio
        point.ordonne = point.ordonnee*y_ratio

    dessin1 = DrawingRectangle(screen, left, top, width, height)
    dessin1.draw()

    return dessin1, new_points


def _get_galerie(screen):

    clear_screen(screen)

    x_dimension, y_dimension = screen.get_size()

    left = 0
    top = 0
    width = x_dimension//2
    height = y_dimension//2
    dessin1, new_points1 = _affichage_image(screen, "galerie/file1.dump",
                                            left, top, width, height, x_dimension, y_dimension)

    left = x_dimension//2
    top = 0
    width = x_dimension//2
    height = y_dimension//2
    dessin2, new_points2 = _affichage_image(screen, "galerie/file2.dump",
                                            left, top, width, height, x_dimension, y_dimension)

    left = 0
    top = y_dimension//2
    width = x_dimension//2
    height = y_dimension//2
    dessin3, new_points3 = _affichage_image(screen, "galerie/file3.dump",
                                            left, top, width, height, x_dimension, y_dimension)

    left = x_dimension//2
    top = y_dimension//2
    width = x_dimension//2
    height = y_dimension//2
    dessin4, new_points4 = _affichage_image(screen, "galerie/file4.dump",
                                            left, top, width, height, x_dimension, y_dimension)

    run = True
    while run:
        dessin1.draw_points(new_points1)
        dessin2.draw_points(new_points2)
        dessin3.draw_points(new_points3)
        dessin4.draw_points(new_points4)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if dessin1.collidepoint(event.pos):
                    return new_points1
                if dessin2.collidepoint(event.pos):
                    return new_points2
                if dessin3.collidepoint(event.pos):
                    return new_points3
                if dessin4.collidepoint(event.pos):
                    return new_points4
        pg.display.update()

def _choose_input_file(screen):
    """
    fonction pour faire choisir à l'utilisateur une image

    screen : surface de l'écran

    return : le chemin vers le fichier
    """
    #top = tkinter.Tk()
    #top.withdraw()
    #file_name = tkinter.filedialog.askopenfilename(parent=top)
    #top.destroy()
    #x_dimension, y_dimension = screen.get_size()
    #not_existing_file = True
    #while(not_existing_file):

    #TODO : a faire

    file_name = "./test.png"
    return file_name

def _choose_and_process_image_file(screen):
    """
    fonction permettant de choisir une image stockée sur la machine
    et de la transformer en liste de points ordonnées

    screen : la surface de l'écran

    return : la liste des point2D ordonnés
    """

    clear_screen(screen)

    valid_file = False
    while(not valid_file):
        filename = _choose_input_file(screen)
        if(filename != ""):
            valid_file = True
    #print(filename)
    
    #process

    #bitmap_inter = _image_to_bitmap(filename)
    bitmap_array = open_bitmap_image(filename)
    points_list = bitmap_to_points(bitmap_array, screen)

    return points_list

def get_points(screen) -> list[Point2D]:
    """
        Fonction qui renvoie une liste de Point2D
        en fonction du choix de l'utilisateur et/ou de son tracer

        screen : la surface Pygame sur laquelle l'utilisateur va dessiner ou choisir son dessin

        return : la liste de Point2D que l'utilisateur à choisit ou dessiné
    """

    clear_screen(screen)

    x_dimension, y_dimension = screen.get_size()

    width = x_dimension*0.50
    height = y_dimension*0.10
    left = x_dimension//2-width//2
    top = y_dimension//2-height
    choix1 = TextBox(screen, left, top, width, height)
    choix1.set_text(_("Draw your own design"))

    left2 = x_dimension//2-width//2
    top2 = y_dimension//2+height
    choix2 = TextBox(screen, left2, top2, width, height)
    choix2.set_text(_("Choose a design to trace"))

    left3 = x_dimension//2-width//2
    top3 = y_dimension//2-3*height
    choix3 = TextBox(screen, left3, top3, width, height)
    choix3.set_text(_("Import your image"))

    run = True
    while run:
        choix1.draw()
        choix2.draw()
        choix3.draw()
        events = pg.event.get()
        for event in events:
            if event.type == pg.QUIT:
                pg.quit()
                run = False
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                if choix1.collidepoint(event.pos):
                    return _get_points_manually(screen)
                if choix2.collidepoint(event.pos):
                    return _get_galerie(screen)
                if choix3.collidepoint(event.pos):
                    return _choose_and_process_image_file(screen)
        pg.display.update()


def sampling_points(points, number_of_points):
    """Retourne une liste échantilloné des points

        points : la liste des points à échantilloner
        number_of_points : le nombre de points à échantilloner

        return : la liste de Point2D échantillonée
    """

    points_length = len(points)

    if number_of_points > points_length:
        return points

    sampling = [points[round(i)] for i in
                linspace(0, points_length, number_of_points - 1, endpoint=False)]

    if sampling:
        sampling.append(sampling[0])

    return sampling
