#!/usr/bin/env python3
"""
Fichier main du projet pao "dessine moi un éléphant".
"""
import sys
import pygame as pg
import pygame_widgets
from pygame_widgets.widget import WidgetHandler

from dessiner_des_elephants.ihm.affichage.screen_utils import init_window, clear_screen
from dessiner_des_elephants.ihm.acquisition.points_acquisition import get_points, \
                                                                      sampling_points
from dessiner_des_elephants.ihm.affichage.constructed_rectangles import ConstructedRectangles

from dessiner_des_elephants.ihm.acquisition.create_slider import create_sampling_slider,\
                                                                 create_number_circle_slider

from dessiner_des_elephants.logique_metier.point import Point2D

def _get_parameters_from_box(screen : pg.Surface, \
                             constructed_rectangle : ConstructedRectangles,\
                             events : list[pg.event.Event]):

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
                clear_screen(screen)

            elif number_circle_box.collidepoint(event.pos):
                number_circle = number_circle_box.get_number_input()
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

def _get_parameters(screen : pg.Surface, points : list[Point2D],\
                    constructed_rectangle : ConstructedRectangles,\
                    number_points : int, number_circle : int):

    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    sampling_box = constructed_rectangle.sampling_box
    number_circle_box = constructed_rectangle.number_circle_box

    sampling_box.slider = create_sampling_slider(screen, constructed_rectangle, points)
    number_circle_box.slider = create_number_circle_slider(screen, constructed_rectangle)

    not_done = True

    sampled_points = points

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

        _show_parameters_box(constructed_rectangle)
        _show_quit_and_start_box(constructed_rectangle)
        _show_drawing_rectangle(constructed_rectangle)
        original_drawing_rectangle.draw_points(sampled_points)

        events = pg.event.get()

        not_done, new_number_points, new_number_circle, new_points = _get_parameters_from_box(\
                                                                     screen,\
                                                                     constructed_rectangle, events)

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

def _launch_drawing(screen : pg.Surface, constructed_rectangle : ConstructedRectangles,\
                    points : list[Point2D],\
                    number_point = None, number_circle = None):
    _show_parameters_box(constructed_rectangle)
    _show_drawing_rectangle(constructed_rectangle)

    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    reconstructed_drawing_rectangle = constructed_rectangle.reconstructed_drawing_rectangle

    original_drawing_rectangle.draw_points(points)

    sampled_points, number_circle, points = _get_parameters(screen, points,\
                                                    constructed_rectangle,\
                                                    number_point, number_circle)

    reconstitue_points = reconstructed_drawing_rectangle.draw_reconstructed_drawing( \
        original_drawing_rectangle, sampled_points, number_circle)

    return len(sampled_points), number_circle, points, reconstitue_points

def _show_quit_and_start_box(constructed_rectangle : ConstructedRectangles):
    start_box = constructed_rectangle.start_box
    quit_box = constructed_rectangle.quit_box

    start_box.draw()
    start_box.set_text("GO !")
    quit_box.draw()
    quit_box.set_text("Quitter")

def _show_parameters_box(constructed_rectangle : ConstructedRectangles):
    number_circle_box = constructed_rectangle.number_circle_box
    sampling_box = constructed_rectangle.sampling_box
    redraw_box = constructed_rectangle.redraw_box

    redraw_box.draw()
    redraw_box.set_text("Changer le dessin")
    sampling_box.draw()
    number_circle_box.draw()

def _show_drawing_rectangle(constructed_rectangle : ConstructedRectangles):
    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    reconstructed_drawing_rectangle = constructed_rectangle.reconstructed_drawing_rectangle

    original_drawing_rectangle.draw()
    reconstructed_drawing_rectangle.draw()

def _launch_main()->None:

    pg.init()

    screen = init_window()
    points = get_points(screen)
    clear_screen(screen)
    pg.display.update()

    constructed_rectangle = ConstructedRectangles(screen)
    last_number_point, last_number_circle, points, reconstitue_points =\
                                                     _launch_drawing(screen,\
                                                     constructed_rectangle, points)

    end = False

    while not end:

        ## Fonction pour afficher les informations.

        last_number_point, last_number_circle, points, reconstitue_points =\
                                                                            _launch_drawing(screen,\
                                                                            constructed_rectangle,\
                                                                            points,\
                                                                            last_number_point,\
                                                                            last_number_circle)

def main()->None:
    """ Ensemble des instruction faite par le programme main """
    _launch_main()

if __name__ == "__main__":
    main()
