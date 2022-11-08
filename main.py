#!/usr/bin/env python3
"""
Fichier main du projet pao "dessine moi un éléphant".
"""

def _get_parameters(screen, points, constructed_rectangle):

    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    sampling_box = constructed_rectangle.sampling_box
    number_circle_box = constructed_rectangle.number_circle_box
    start_box = constructed_rectangle.start_box

    width_slider = constructed_rectangle.box_padding_ordinate // 2
    height_slider = constructed_rectangle.box_width

    left_slider_sampling = sampling_box.left
    top_slider_sampling = sampling_box.top + sampling_box.height \
                          + (constructed_rectangle.box_padding_ordinate // 4)

    slider_sampling = Slider(screen, left_slider_sampling, top_slider_sampling, \
                             width_slider, height_slider)
    #slider_sampling.draw()

    not_done = True

    number_circle = 1
    sampled_points = points
    while not_done:
        clear_screen(screen)

        _show_parameters_box(constructed_rectangle)
        _show_drawing_rectangle(constructed_rectangle)
        original_drawing_rectangle.draw_points(sampled_points)

        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                exit()

            if event.type == pg.KEYDOWN:
                if event.key == pg.K_q:
                    exit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1: # If the button pressed is the left one
                    if sampling_box.collidepoint(event.pos):
                        number_points = sampling_box.get_number_input()

                        sampled_points = sampling_points(points, number_points)

                    elif number_circle_box.collidepoint(event.pos):
                        number_circle = number_circle_box.get_number_input()

                    elif start_box.collidepoint(event.pos):
                        if number_circle > 0:
                            not_done = False

        pg.display.update()
        #pygame_widgets.update(events)
        


    return sampled_points, number_circle

def _launch_drawing(screen, constructed_rectangle, points):
    clear_screen(screen)
    _show_parameters_box(constructed_rectangle)
    _show_drawing_rectangle(constructed_rectangle)

    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    reconstructed_drawing_rectangle = constructed_rectangle.reconstructed_drawing_rectangle

    original_drawing_rectangle.draw_points(points)

    sampled_points, number_circle = _get_parameters(screen, points, constructed_rectangle)

    reconstructed_drawing_rectangle.draw_reconstructed_drawing( \
        original_drawing_rectangle, sampled_points, number_circle)

def _show_parameters_box(constructed_rectangle):
    start_box = constructed_rectangle.start_box
    number_circle_box = constructed_rectangle.number_circle_box
    sampling_box = constructed_rectangle.sampling_box

    sampling_box.draw()
    number_circle_box.draw()
    start_box.draw()
    start_box.set_text("GO !")

def _show_drawing_rectangle(constructed_rectangle):
    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    reconstructed_drawing_rectangle = constructed_rectangle.reconstructed_drawing_rectangle

    original_drawing_rectangle.draw()
    reconstructed_drawing_rectangle.draw()

def _show_draw_box(constructed_rectangle):
    draw_box = constructed_rectangle.draw_box
    redraw_box = constructed_rectangle.redraw_box

    draw_box.draw()
    draw_box.set_text("DRAW")
    redraw_box.draw()
    redraw_box.set_text("REDRAW")

def _launch_main():
    
    pg.init()

    screen = init_window()
    constructed_rectangle = ConstructedRectangles(screen)
    points = get_points(screen)

    _launch_drawing(screen, constructed_rectangle, points)

    _show_draw_box(constructed_rectangle)

    draw_box = constructed_rectangle.draw_box
    redraw_box = constructed_rectangle.redraw_box

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
                    if draw_box.collidepoint(event.pos):
                        _launch_drawing(screen, constructed_rectangle, points)
                        _show_draw_box(constructed_rectangle)

                    if redraw_box.collidepoint(event.pos):
                        points = get_points(screen)
                        _launch_drawing(screen, constructed_rectangle, points)
                        _show_draw_box(constructed_rectangle)


if __name__ == "__main__":

    from dessiner_des_elephants.ihm.affichage.screen_utils import init_window, clear_screen
    from dessiner_des_elephants.ihm.acquisition.points_acquisition import get_points, \
                                                                          sampling_points
    from dessiner_des_elephants.ihm.affichage.constructed_rectangles import ConstructedRectangles

    import pygame as pg
    import pygame_widgets
    from pygame_widgets.slider import Slider

    _launch_main()
