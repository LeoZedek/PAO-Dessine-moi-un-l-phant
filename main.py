#!/usr/bin/env python3
"""
Fichier main du projet pao "dessine moi un éléphant".
"""

def _get_parameters(points, constructed_rectangle):

    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    sampling_box = constructed_rectangle.sampling_box
    number_circle_box = constructed_rectangle.number_circle_box
    start_box = constructed_rectangle.start_box

    not_done = True

    number_circle = 1
    sampled_points = points
    while not_done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                not_done = False

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    not_done = False

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1: # If the button pressed is the left one
                    if sampling_box.collidepoint(event.pos):
                        number_points = sampling_box.get_number_input()

                        sampled_points = sampling_points(points, number_points)
                        original_drawing_rectangle.clear()
                        original_drawing_rectangle.draw_points(sampled_points)

                    elif number_circle_box.collidepoint(event.pos):
                        number_circle = number_circle_box.get_number_input()

                    elif start_box.collidepoint(event.pos):
                        not_done = False

            pg.display.update()

    return sampled_points, number_circle

def _launch_drawing(screen):
    clear_screen(screen)

    points = get_points(screen)

    clear_screen(screen)

    ## Construction of the input box
    constructed_rectangle = ConstructedRectangles(screen)

    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    reconstructed_drawing_rectangle = constructed_rectangle.reconstructed_drawing_rectangle

    original_drawing_rectangle.draw_points(points)

    sampled_points, number_circle = _get_parameters(points, constructed_rectangle)

    reconstructed_drawing_rectangle.draw_reconstructed_drawing( \
        original_drawing_rectangle, sampled_points, number_circle)

    return constructed_rectangle.redraw_box

def _launch_main():
    
    pg.init()

    screen = init_window()

    redraw_box = _launch_drawing(screen)

    redraw_box.draw()
    redraw_box.set_text("DRAW")

    end = False

    while not end:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                end = True

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    end = True
                if event.key == pg.K_y:
                    _launch_drawing(screen)

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1: # If the button pressed is the left one
                    if redraw_box.collidepoint(event.pos):
                        _launch_drawing(screen)

if __name__ == "__main__":

    from dessiner_des_elephants.ihm.affichage.screen_utils import init_window, clear_screen
    from dessiner_des_elephants.ihm.acquisition.points_acquisition import get_points, \
                                                                          sampling_points
    from dessiner_des_elephants.ihm.affichage.constructed_rectangles import ConstructedRectangles

    import pygame as pg

    _launch_main()
