#!/usr/bin/env python3
"""
Module présentant les fonctions nécessaires à l'affichage des rectangles du main
"""
from dessiner_des_elephants.traduction import _

from dessiner_des_elephants.ihm.affichage.constructed_rectangles import ConstructedRectangles


def show_quit_and_start_box(constructed_rectangle: ConstructedRectangles):
    '''
        Fonction qui affiche les rectanges start et quit

        constructed_rectangle : L'objet ConstructedRectangle qui contient tous les rectangles
    '''
    start_box = constructed_rectangle.start_box
    quit_box = constructed_rectangle.quit_box

    start_box.draw()
    start_box.set_text(_("GO !"))
    quit_box.draw()
    quit_box.set_text(_("Quit"))


def show_parameters_box(constructed_rectangle: ConstructedRectangles) -> None:
    '''
        Fonction qui affiche les rectanges redraw, sampling et number_circle

        constructed_rectangle : L'objet ConstructedRectangle qui contient tous les rectangles
    '''
    number_circle_box = constructed_rectangle.number_circle_box
    sampling_box = constructed_rectangle.sampling_box
    redraw_box = constructed_rectangle.redraw_box

    redraw_box.draw()
    redraw_box.set_text(_("Change the design"))
    sampling_box.draw()
    number_circle_box.draw()


def show_drawing_rectangle(constructed_rectangle: ConstructedRectangles) -> None:
    '''
        Fonction qui affiche les rectanges original_drawing et reconstructed_drawing

        constructed_rectangle : L'objet ConstructedRectangle qui contient tous les rectangles
    '''
    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    reconstructed_drawing_rectangle = constructed_rectangle.reconstructed_drawing_rectangle

    original_drawing_rectangle.draw()
    reconstructed_drawing_rectangle.draw()
