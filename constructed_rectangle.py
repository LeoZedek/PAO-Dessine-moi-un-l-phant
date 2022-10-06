#!/usr/bin/env python3
"""Module permettant de construire les différents rectangle"""

from draw_elephant_utils import PROPORTION_ORIGINAL_DRAWING, INPUT_SAMPLING_BOX_WIDTH
from draw_elephant_utils import INPUT_SAMPLING_BOX_PADDING_RIGHT, INPUT_SAMPLING_BOX_PADDING_TOP
from draw_elephant_utils import INPUT_SAMPLING_BOX_HEIGHT
from input_box import InputBox
from drawing_rectangle import DrawingRectangle

def create_drawing_rectangles(screen):

    x_dimension, y_dimension = screen.get_size()

    top_original_drawing_rect = 0
    left_original_drawing_rect = 0
    height_original_drawing_rect = y_dimension * PROPORTION_ORIGINAL_DRAWING
    width_original_drawing_rect = x_dimension * PROPORTION_ORIGINAL_DRAWING

    original_drawing_rectangle = DrawingRectangle(screen, left_original_drawing_rect,\
        top_original_drawing_rect, width_original_drawing_rect, height_original_drawing_rect)

    ## Construction of the reconstructed drawing rectangle

    top_reconstructed_drawing_rect = height_original_drawing_rect - 1
    left_reconstructed_drawing_rect = width_original_drawing_rect - 1
    width_reconstructed_drawing_rect = x_dimension - left_reconstructed_drawing_rect + 1
    height_reconstructed_drawing_rect = y_dimension - top_reconstructed_drawing_rect + 1

    reconstructed_drawing_rectangle = DrawingRectangle(screen, left_reconstructed_drawing_rect,\
     top_reconstructed_drawing_rect, width_reconstructed_drawing_rect, \
     height_reconstructed_drawing_rect)

    return original_drawing_rectangle, reconstructed_drawing_rectangle

def create_sampling_box(screen):

    x_dimension, y_dimension = screen.get_size()

    height_original_drawing_rect = y_dimension * PROPORTION_ORIGINAL_DRAWING
    width_original_drawing_rect = x_dimension * PROPORTION_ORIGINAL_DRAWING

    padding_top_box = round(height_original_drawing_rect * INPUT_SAMPLING_BOX_PADDING_TOP)
    padding_left_box = round(width_original_drawing_rect * INPUT_SAMPLING_BOX_PADDING_RIGHT)
    box_height = round(INPUT_SAMPLING_BOX_HEIGHT * height_original_drawing_rect)
    box_width = round(INPUT_SAMPLING_BOX_WIDTH * width_original_drawing_rect)

    top_sampling_box = padding_top_box
    left_sampling_box = width_original_drawing_rect + padding_left_box
    height_sampling_box = box_height
    width_sampling_box = box_width

    sampling_box = InputBox(screen, left_sampling_box, \
        top_sampling_box, width_sampling_box, height_sampling_box)
    sampling_box.draw()

    return sampling_box

def create_number_circle_box(screen):
    

def create_input_boxes(screen):
    x_dimension, y_dimension = screen.get_size()

    

    top_reconstructed_drawing_rect = height_original_drawing_rect - 1
    left_reconstructed_drawing_rect = width_original_drawing_rect - 1
    width_reconstructed_drawing_rect = x_dimension - left_reconstructed_drawing_rect + 1
    height_reconstructed_drawing_rect = y_dimension - top_reconstructed_drawing_rect + 1

    padding_top_box = round(height_original_drawing_rect * INPUT_SAMPLING_BOX_PADDING_TOP)
    padding_left_box = round(width_original_drawing_rect * INPUT_SAMPLING_BOX_PADDING_RIGHT)
    box_height = round(INPUT_SAMPLING_BOX_HEIGHT * height_original_drawing_rect)
    box_width = round(INPUT_SAMPLING_BOX_WIDTH * width_original_drawing_rect)

    top_sampling_box = padding_top_box
    left_sampling_box = width_original_drawing_rect + padding_left_box
    height_sampling_box = box_height
    width_sampling_box = box_width

    sampling_box = InputBox(screen, left_sampling_box, \
        top_sampling_box, width_sampling_box, height_sampling_box)
    sampling_box.draw()

    height_number_circle_box = box_height
    width_number_circle_box = box_width
    top_number_circle_box = top_reconstructed_drawing_rect - padding_top_box - box_height
    left_number_circle_box = x_dimension - padding_left_box - box_width

    number_circle_box = InputBox(screen, left_number_circle_box, \
        top_number_circle_box, width_number_circle_box, height_number_circle_box)
    number_circle_box.draw()

    height_start_box = box_height
    width_start_box = box_width
    top_start_box = top_reconstructed_drawing_rect \
        + height_reconstructed_drawing_rect // 2 - height_start_box // 2
    left_start_box = x_dimension - padding_left_box - box_width

    start_box = InputBox(screen, left_start_box, \
        top_start_box, width_start_box, height_start_box)
    start_box.draw()
    start_box.set_text("GO !")

    return sampling_box, number_circle_box, start_box