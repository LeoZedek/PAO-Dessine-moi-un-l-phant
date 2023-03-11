#!/usr/bin/env python3
"""
Fichier main du projet pao "dessine moi un éléphant".
"""
# Importation externe
import pygame as pg
from dessiner_des_elephants.traduction import _

# Importation interne
from dessiner_des_elephants.ihm.affichage.screen_utils import init_window, clear_screen
from dessiner_des_elephants.ihm.affichage.constructed_rectangles import ConstructedRectangles

from dessiner_des_elephants.ihm.affichage.show_boxes import show_parameters_box,\
    show_drawing_rectangle

from dessiner_des_elephants.ihm.acquisition.points_acquisition import get_points
from dessiner_des_elephants.ihm.acquisition.get_parameters import get_parameters

from dessiner_des_elephants.logique_metier.point import Point2D
from dessiner_des_elephants.ihm.affichage.text_box import TextBox


def _launch_drawing(screen: pg.Surface, constructed_rectangle: ConstructedRectangles,
                    points: list[Point2D],
                    number_point=None, number_circle=None):
    show_parameters_box(constructed_rectangle)
    show_drawing_rectangle(constructed_rectangle)

    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    reconstructed_drawing_rectangle = constructed_rectangle.reconstructed_drawing_rectangle

    original_drawing_rectangle.draw_points(points)

    sampled_points, number_circle, points = get_parameters(screen, points,
                                                           constructed_rectangle,
                                                           number_point, number_circle)

    reconstitue_points = reconstructed_drawing_rectangle.draw_reconstructed_drawing(
        original_drawing_rectangle, sampled_points, number_circle)

    return len(sampled_points), number_circle, points, reconstitue_points


def _launch_main() -> None:

    pg.init()

    screen = init_window()
    points = get_points(screen)
    nb_points_total = len(points)
    clear_screen(screen)
    pg.display.update()

    constructed_rectangle = ConstructedRectangles(screen)
    #constructed_rectangle.top_left_rectangle.draw_points(points)
    last_number_point, last_number_circle, points, reconstitue_points =\
        _launch_drawing(screen,
                        constructed_rectangle, points)

    end = False

    while not end:

        last_number_point, last_number_circle, points, reconstitue_points =\
            _launch_drawing(screen,
                            constructed_rectangle,
                            points,
                            last_number_point,
                            last_number_circle)


def main() -> None:
    """ Ensemble des instruction faite par le programme main """
    # Lancement du programme
    _launch_main()


if __name__ == "__main__":
    main()
