#!/usr/bin/env python3
"""Module permettant de construire les différents rectangle"""

from draw_elephant_utils import PROPORTION_ORIGINAL_DRAWING, INPUT_SAMPLING_BOX_WIDTH
from draw_elephant_utils import INPUT_SAMPLING_BOX_PADDING_RIGHT, INPUT_SAMPLING_BOX_PADDING_TOP
from draw_elephant_utils import INPUT_SAMPLING_BOX_HEIGHT
from input_box import InputBox
from drawing_rectangle import DrawingRectangle

class ConstructedRectangle:

    def __init__(self, screen):

        self._screen = screen
        self._x_dimension, self._y_dimension = screen.get_size()

        self._original_drawing_rectangle, self._reconstructed_drawing_rectangle = \
            self._constructed_drawing_rect()

        self._box_width, self._box_height = self._constructed_box_dimension()

        self._box_padding_abscissa, self._box_padding_ordinate = \
            self._constructed_box_padding()

    @property
    def screen(self)->pg.Surface:
        return self._screen

    @property
    def x_dimension(self)->int:
        return self._x_dimension

    @property
    def y_dimension(self)->int:
        return self._y_dimension

    @property
    def original_drawing_rectangle(self):
        return self._original_drawing_rect

    @property
    def reconstructed_drawing_rectangle(self):
        return self._reconstructed_drawing_rectangle

    @property
    def box_width(self)->int:
        return self._box_width

    @property
    def box_height(self)->int:
        return self._box_height

    @property
    def box_padding_abscissa(self)->int:
        return self._box_padding_abscissa

    @property
    def box_padding_ordinate(self)->int:
        return self._box_padding_ordinate
    

    def _constructed_drawing_rect(self):
        top_original_drawing_rect = 0
        left_original_drawing_rect = 0
        height_original_drawing_rect = y_dimension * PROPORTION_ORIGINAL_DRAWING
        width_original_drawing_rect = x_dimension * PROPORTION_ORIGINAL_DRAWING

        original_drawing_rectangle = DrawingRectangle(screen, left_original_drawing_rect,\
            top_original_drawing_rect, width_original_drawing_rect, height_original_drawing_rect)

        top_reconstructed_drawing_rect = height_original_drawing_rect - 1
        left_reconstructed_drawing_rect = width_original_drawing_rect - 1
        width_reconstructed_drawing_rect = x_dimension - left_reconstructed_drawing_rect + 1
        height_reconstructed_drawing_rect = y_dimension - top_reconstructed_drawing_rect + 1

        reconstructed_drawing_rectangle = DrawingRectangle(screen, left_reconstructed_drawing_rect,\
            top_reconstructed_drawing_rect, width_reconstructed_drawing_rect, \
            height_reconstructed_drawing_rect)

        return original_drawing_rectangle, reconstructed_drawing_rectangle

    def _constructed_box_dimension(self):
        box_height = round(INPUT_SAMPLING_BOX_HEIGHT * self.original_drawing_rectangle.height)
        box_width = round(INPUT_SAMPLING_BOX_WIDTH * self.original_drawing_rectangle.width)

        return box_width, box_height

    def _constructed_box_padding(self):
        padding_abscissa_box = round(self.original_drawing_rectangle.width * INPUT_SAMPLING_BOX_PADDING_RIGHT)
        padding_ordinate_box = round(self.original_drawing_rectangle.height * INPUT_SAMPLING_BOX_PADDING_TOP)

        return padding_abscissa_box, padding_ordinate_box

    def _constructed_sampling_box(self):

        top_sampling_box = self.box_padding_ordinate
        left_sampling_box = self.box_padding_abscissa + self.original_drawing_rectangle.width
        height_sampling_box = self.box_height
        width_sampling_box = self.box_width

        sampling_box = InputBox(screen, left_sampling_box, \
            top_sampling_box, width_sampling_box, height_sampling_box)
        sampling_box.draw()

        return sampling_box


def get_box_dimension(screen):

    x_dimension, y_dimension = screen.get_size()

    height_original_drawing_rect = y_dimension * PROPORTION_ORIGINAL_DRAWING
    width_original_drawing_rect = x_dimension * PROPORTION_ORIGINAL_DRAWING

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

    top_sampling_box = round(height_original_drawing_rect * INPUT_SAMPLING_BOX_PADDING_TOP)
    left_sampling_box = width_original_drawing_rect * (1 + INPUT_SAMPLING_BOX_PADDING_RIGHT)
    height_sampling_box = round(INPUT_SAMPLING_BOX_HEIGHT * height_original_drawing_rect)
    width_sampling_box = round(INPUT_SAMPLING_BOX_WIDTH * width_original_drawing_rect)

    sampling_box = InputBox(screen, left_sampling_box, \
        top_sampling_box, width_sampling_box, height_sampling_box)
    sampling_box.draw()

    return sampling_box

def create_number_circle_box(screen):

    x_dimension, y_dimension = screen.get_size()

    height_original_drawing_rect = y_dimension * PROPORTION_ORIGINAL_DRAWING
    width_original_drawing_rect = x_dimension * PROPORTION_ORIGINAL_DRAWING

    height_number_circle_box = box_height
    width_number_circle_box = box_width
    top_number_circle_box = top_reconstructed_drawing_rect - padding_top_box - box_height
    left_number_circle_box = x_dimension - padding_left_box - box_width

    number_circle_box = InputBox(screen, left_number_circle_box, \
        top_number_circle_box, width_number_circle_box, height_number_circle_box)
    number_circle_box.draw()

    return create_number_circle_box

def start_box(screen):
    x_dimension, y_dimension = screen.get_size()

    height_original_drawing_rect = y_dimension * PROPORTION_ORIGINAL_DRAWING
    width_original_drawing_rect = x_dimension * PROPORTION_ORIGINAL_DRAWING

    height_start_box = box_height
    width_start_box = box_width
    top_start_box = top_reconstructed_drawing_rect \
        + height_reconstructed_drawing_rect // 2 - height_start_box // 2
    left_start_box = x_dimension - padding_left_box - box_width

    start_box = InputBox(screen, left_start_box, \
        top_start_box, width_start_box, height_start_box)
    start_box.draw()
    start_box.set_text("GO !")

    return start_box

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