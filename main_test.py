#!/usr/bin/env python3
"""
Fichier main du projet pao "dessine moi un éléphant".
"""

def _create_sampling_slider(screen, constructed_rectangle, points):
    sampling_box = constructed_rectangle.sampling_box

    width_slider = constructed_rectangle.box_width
    height_slider = constructed_rectangle.box_padding_ordinate // 2

    left_slider_sampling = sampling_box.left
    top_slider_sampling = sampling_box.top + sampling_box.height \
                          + (constructed_rectangle.box_padding_ordinate // 4)

    min_sampling = min(len(points), 10)
    max_sampling = min(len(points), 2000)

    slider_sampling = Slider(screen, left_slider_sampling, top_slider_sampling, \
                             width_slider, height_slider, \
                             min = min_sampling, max = max_sampling, \
                             step = 5, \
                             handleColour = SLIDER_HANDLE_COLOR, colour = SLIDER_COLOR)
    return slider_sampling

def _create_number_circle_slider(screen, constructed_rectangle):

    number_circle_box = constructed_rectangle.number_circle_box

    width_slider = constructed_rectangle.box_width
    height_slider = constructed_rectangle.box_padding_ordinate // 2

    left_slider_number_circle = number_circle_box.left
    top_slider_number_circle = number_circle_box.top + number_circle_box.height \
                          + (constructed_rectangle.box_padding_ordinate // 4)

    slider_number_circle = Slider(screen, left_slider_number_circle, \
                             top_slider_number_circle, width_slider, height_slider, \
                             min = MIN_CIRCLE, max = MAX_CIRCLE, \
                             step = 1, \
                             handleColour = SLIDER_HANDLE_COLOR, colour = SLIDER_COLOR)
    return slider_number_circle

def _get_parameters(screen, points, constructed_rectangle,\
                    number_points, number_circle):

    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    sampling_box = constructed_rectangle.sampling_box
    number_circle_box = constructed_rectangle.number_circle_box
    start_box = constructed_rectangle.start_box

    slider_sampling = _create_sampling_slider(screen, constructed_rectangle, points)
    slider_number_circle = _create_number_circle_slider(screen, constructed_rectangle)

    sampling_box.slider = slider_sampling
    number_circle_box.slider = slider_number_circle

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
        clear_screen(screen)

        _show_parameters_box(constructed_rectangle)
        _show_drawing_rectangle(constructed_rectangle)
        original_drawing_rectangle.draw_points(sampled_points)

        events = pg.event.get()

        for event in events:
            if event.type == pg.QUIT:
                sys.exit()

            if event.type == pg.KEYDOWN and event.key == pg.K_q:
                sys.exit()

            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            # If the button pressed is the left one

                if sampling_box.collidepoint(event.pos):
                    number_points = sampling_box.get_number_input()

                    sampled_points = sampling_points(points, number_points)

                elif number_circle_box.collidepoint(event.pos):
                    number_circle = number_circle_box.get_number_input()

                elif start_box.collidepoint(event.pos):
                    if number_circle and number_circle > 0:
                        not_done = False

        if sampling_box.update():
            number_points = sampling_box.value
            sampled_points = sampling_points(points, number_points)

        if number_circle_box.update():
            number_circle = number_circle_box.value

        pygame_widgets.update(events)
        pg.display.update()

    WidgetHandler.removeWidget(slider_sampling)
    WidgetHandler.removeWidget(slider_number_circle)

    number_circle = number_circle_box.value

    number_points = sampling_box.value
    sampled_points = sampling_points(points, number_points)

    return sampled_points, number_circle

def _launch_drawing(screen, constructed_rectangle, points,\
                    number_point = None, number_circle = None):
    clear_screen(screen)
    _show_parameters_box(constructed_rectangle)
    _show_drawing_rectangle(constructed_rectangle)

    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    reconstructed_drawing_rectangle = constructed_rectangle.reconstructed_drawing_rectangle

    original_drawing_rectangle.draw_points(points)

    sampled_points, number_circle = _get_parameters(screen, points, constructed_rectangle,\
                                                    number_point, number_circle)

    reconstructed_drawing_rectangle.draw_reconstructed_drawing( \
        original_drawing_rectangle, sampled_points, number_circle)

    return len(sampled_points), number_circle

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

def _show_draw_boxes(constructed_rectangle):
    draw_box = constructed_rectangle.draw_box
    redraw_box = constructed_rectangle.redraw_box
    quit_box = constructed_rectangle.quit_box

    quit_box.draw()
    quit_box.set_text("QUIT")
    draw_box.draw()
    draw_box.set_text("DRAW")
    redraw_box.draw()
    redraw_box.set_text("REDRAW")

def _launch_main():

    pg.init()

    screen = init_window()
    points = get_points(screen)

    file = open("file.txt", "wb")

    pickle.dump(points, file, protocol = pickle.DEFAULT_PROTOCOL)

    file.close()

    file = open("file.txt", "rb")

    new_points = pickle.load(file)

    file.close()

    print(new_points)

    clear_screen(screen)

if __name__ == "__main__":

    from dessiner_des_elephants.ihm.affichage.screen_utils import init_window, clear_screen
    from dessiner_des_elephants.ihm.acquisition.points_acquisition import get_points, \
                                                                          sampling_points
    from dessiner_des_elephants.ihm.affichage.constructed_rectangles import ConstructedRectangles
    from dessiner_des_elephants.ihm.affichage.draw_elephant_utils import SLIDER_COLOR,\
                                                                         SLIDER_HANDLE_COLOR, \
                                                                         MIN_CIRCLE, MAX_CIRCLE
    import sys
    import pygame as pg
    import pygame_widgets
    from pygame_widgets.slider import Slider
    from pygame_widgets.widget import WidgetHandler
    import pickle

    _launch_main()
