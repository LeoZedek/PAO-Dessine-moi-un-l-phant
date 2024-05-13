#!/usr/bin/env python3
"""
Module présentant les fonctions nécessaires à l'affichage des rectangles du main
"""
from dessiner_des_elephants.traduction import _

from dessiner_des_elephants.ihm.affichage.constructed_rectangles import ConstructedRectangles
from dessiner_des_elephants.logique_metier.taux_compression import compression_rate_sampling, \
        compression_rate_circles


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
    top_left_rectangle = constructed_rectangle.top_left_rectangle

    original_drawing_rectangle.draw()
    reconstructed_drawing_rectangle.draw()
    top_left_rectangle.draw()


def show_drawing_title_box(constructed_rectangle: ConstructedRectangles, number_points : int, number_sampled_points: int, number_circles: int) -> None:
    '''
        Fonction qui affiche rectangles de titre de drawing

        constructed_rectangle : L'objet ConstructedRectangle qui contient tous les rectangles
        points : liste des points
        number_sampled_points : nombre points échantillonés
        number_circles : nombre de cercles
    '''

    aquired_title = constructed_rectangle.aquired_drawing_title_box
    sampled_title = constructed_rectangle.sampled_drawing_title_box
    circles_title = constructed_rectangle.circles_drawing_title_box
    
    aquired_title.set_text(
            f"aquired drawing : {number_points*16/1024:.2f} ko ({number_points} points)")
    sampled_title.set_text(
            f"sampled drawing : {number_sampled_points*16/1024:.2f} ko ({number_sampled_points} points)")
    circles_title.set_text(
            f"reconstructed drawing : {number_circles*16/1024:.2f} ko ({number_circles} circles)")

    aquired_title.draw()
    sampled_title.draw()
    circles_title.draw()

def show_compression_box(constructed_rectangle: ConstructedRectangles, number_points : int, number_sampled_points: int, number_circles: int) -> None:
    '''
        Fonction qui affiche les rectangles de compression

        constructed_rectangle : L'objet ConstructedRectangle qui contient tous les rectangles
        points : liste des points
        number_sampled_points : nombre points échantillonés
        number_circles : nombre de cercles
    '''
    
    compression_sampling = constructed_rectangle.compression_sampling_box
    compression_circles = constructed_rectangle.compression_circles_box

    compression_sampling.set_text(
            f"compression rate sampling : {compression_rate_sampling(number_points, number_sampled_points):.2f} %")
    compression_circles.set_text(
            f"compression rate reconstructed(circles) : {compression_rate_circles(number_points, number_circles):.2f} %")

    compression_circles.draw()
    compression_sampling.draw()
