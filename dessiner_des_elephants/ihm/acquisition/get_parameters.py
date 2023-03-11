#!/usr/bin/env python3
"""
Module proposant la fonction get_parameters qui renvoie les paramètres
(points, nombre de points et nombre de cercles) choisit par l'utilisateur
"""

import sys
import pygame as pg
import pygame_widgets
from pygame_widgets.widget import WidgetHandler

from dessiner_des_elephants.ihm.affichage.screen_utils import clear_screen
from dessiner_des_elephants.ihm.acquisition.points_acquisition import get_points, \
    sampling_points
from dessiner_des_elephants.ihm.affichage.constructed_rectangles import ConstructedRectangles

from dessiner_des_elephants.ihm.acquisition.create_slider import create_sampling_slider,\
    create_number_circle_slider

from dessiner_des_elephants.ihm.affichage.show_boxes import show_quit_and_start_box,\
    show_parameters_box,\
    show_drawing_rectangle, \
    show_drawing_title_box, \
    show_compression_box

from dessiner_des_elephants.logique_metier.point import Point2D


def _get_parameters_from_box(screen: pg.Surface,
                             constructed_rectangle: ConstructedRectangles,
                             events: list[pg.event.Event]):

    """
    Check les evénements pygame pour vérifier si l'utilisateur
    veut modifier, la valeur des paramètres

    screen : la pg.Surface où les paramètres sont affiché
    constructed_rectangle : l'objet ConstructedRectangle qui contient tous les rectangles
    events : liste d'objet pg.event.Event qui contient tous les événements pygame

    return : True si l'utilisateur ne sort pas de l'acquisition des paramètres
             False sinon

             Le nombre de points si l'utilisateur a changé le nombre de points
             None sinon

             Le nombre de cercle si l'utilisateur a changé le nombre de cercle
             None sinon

             La liste de Point2D si l'utilisateur a changer le dessin
             None sinon
    """

    sampling_box = constructed_rectangle.sampling_box
    number_circle_box = constructed_rectangle.number_circle_box

    start_box = constructed_rectangle.start_box
    redraw_box = constructed_rectangle.redraw_box
    quit_box = constructed_rectangle.quit_box

    number_points = None
    number_circle = None
    points = None

    not_done = True
    for event in events:

        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            # If the button pressed is the left one

            if sampling_box.collidepoint(event.pos):
                number_points = sampling_box.get_number_input()

                if number_points < 2:
                    number_points = 2
                    sampling_box.set("2")

                clear_screen(screen)

            elif number_circle_box.collidepoint(event.pos):
                number_circle = number_circle_box.get_number_input()

                # On ne veux pas de nombre impaire ou égale à 0
                if number_circle == 0:
                    number_circle = 2
                    number_circle_box.value = number_circle

                #if number_circle % 2 == 1:
                #    number_circle += 1
                #    number_circle_box.value = number_circle

                clear_screen(screen)

            elif start_box.collidepoint(event.pos):
                not_done = False

            elif redraw_box.collidepoint(event.pos):
                points = get_points(screen)
                clear_screen(screen)

            elif quit_box.collidepoint(event.pos):
                sys.exit()

    if sampling_box.update():
        number_points = sampling_box.value

    if number_circle_box.update():
        number_circle = number_circle_box.value

    return not_done, number_points, number_circle, points


def get_parameters(screen: pg.Surface, points: list[Point2D],
                   constructed_rectangle: ConstructedRectangles,
                   number_points: int, number_circle: int):
    """
    Renvoie les paramètres que l'utilisateur à choisit

    screen : L'objet pg.Surface sur lequel l'utilisateur choisit les paramètres
    points : Liste de Point2D à afficher
    constructed_rectangle : L'objet ConstructedRectangle qui contient tous les rectangles
    number_points : ancien nombre de points précedemment choisit par l'utilisateur
    number_circle : ancien nombre de cercles précedemment choisit par l'utilisateur

    return sampled_points : Liste des points échantilloné par nombre_points
           number_circle : Nombre de cercle choisit par l'utilisateur
           points : La liste de Point2D, que l'utilisateur a potentiellement changé
    """
    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    top_left_rectangle = constructed_rectangle.top_left_rectangle
    sampling_box = constructed_rectangle.sampling_box
    number_circle_box = constructed_rectangle.number_circle_box

    sampling_box.slider = create_sampling_slider(
        screen, constructed_rectangle, points)
    number_circle_box.slider = create_number_circle_slider(
        screen, constructed_rectangle)

    not_done = True

    sampled_points = points

    # Pour garder les anciennes valeurs qui ont été mises par l'utilisateur
    if number_points:
        sampling_box.value = number_points
    else:
        number_points = sampling_box.value

    if number_circle:
        number_circle_box.value = number_circle
    else:
        number_circle = number_circle_box.value

    while not_done:
        constructed_rectangle.top_right_rectangle.clear()
        original_drawing_rectangle.clear()

        show_parameters_box(constructed_rectangle)
        show_quit_and_start_box(constructed_rectangle)
        show_drawing_rectangle(constructed_rectangle)
        show_drawing_title_box(constructed_rectangle, len(points), number_points, number_circle) 
        show_compression_box(constructed_rectangle, len(points), number_points, number_circle)
        original_drawing_rectangle.draw_points(sampled_points)
        top_left_rectangle.draw_points(points)

        events = pg.event.get()

        not_done, new_number_points, new_number_circle, new_points = _get_parameters_from_box(
            screen,
            constructed_rectangle, events)

        # Si l'utilisateur à changer les paramètres, on les mets à jours
        if new_points:
            points = new_points

        if new_number_points:
            number_points = new_number_points

        if new_number_circle:
            number_circle = new_number_circle

        sampled_points = sampling_points(points, number_points)

        pygame_widgets.update(events)
        pg.display.update()

    WidgetHandler.removeWidget(sampling_box.slider)
    WidgetHandler.removeWidget(number_circle_box.slider)

    number_circle = number_circle_box.value
    number_points = sampling_box.value
    sampled_points = sampling_points(points, number_points)

    return sampled_points, number_circle, points
