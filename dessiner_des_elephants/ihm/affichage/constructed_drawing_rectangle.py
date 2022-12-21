#!/usr/bin/env python3
"""Module permettant de construire les rectangles de dessins"""

import pygame as pg
from .draw_elephant_utils import PROPORTION_ORIGINAL_DRAWING
from .drawing_rectangle import DrawingRectangle
from .my_rectangle import MyRectangle


class ConstructedDrawingRectangle:
    """
    Classe permettant de construire les differents rectangle de dessin de l'ihm.
    Elle permet de construire les deux rectangles de dessins contenant le dessin original
    et le dessin reconstruit
    """

    def __init__(self, screen):
        """
            screen : Surface pygame de la fenêtre
        """

        self._screen = screen
        self._abscissa_dimension, self._ordinate_dimension = screen.get_size()

        self._original_drawing_rectangle, self._reconstructed_drawing_rectangle = \
            self._constructed_drawing_rect()

        self._top_right_rectangle = self._constructed_top_right_rect()
        self._bottom_left_rectangle = self._constructed_bottom_left_rect()

    @property
    def screen(self) -> pg.Surface:
        """
        Getter pour avoir la Surface
        """
        return self._screen

    @property
    def abscissa_dimension(self) -> int:
        """
        Getter de la dimension de l'abscisse
        """
        return self._abscissa_dimension

    @property
    def ordinate_dimension(self) -> int:
        """
        Getter de la dimension de l'ordonnee
        """
        return self._ordinate_dimension

    @property
    def original_drawing_rectangle(self):
        """
        Getter du rectangle du dessin orginal
        """
        return self._original_drawing_rectangle

    @property
    def reconstructed_drawing_rectangle(self):
        """
        Getter du rectangle du dessin reconstruit
        """
        return self._reconstructed_drawing_rectangle

    @property
    def top_right_rectangle(self):
        """ Getter du rectangle haut droit """
        return self._top_right_rectangle

    @property
    def bottom_left_rectangle(self):
        """ Getter du rectangle bas gauche """
        return self._bottom_left_rectangle

    def _constructed_drawing_rect(self):
        """
        Construit le rectangles où le dessin original sera affiché et
        le rectangle où le dessin reconstruit sera affiché
        """
        top_original_drawing_rect = 0
        left_original_drawing_rect = 0
        height_original_drawing_rect = self.ordinate_dimension * PROPORTION_ORIGINAL_DRAWING
        width_original_drawing_rect = self.abscissa_dimension * PROPORTION_ORIGINAL_DRAWING

        original_drawing_rectangle = DrawingRectangle(self.screen, left_original_drawing_rect,
                                                      top_original_drawing_rect, width_original_drawing_rect, height_original_drawing_rect)

        top_reconstructed_drawing_rect = height_original_drawing_rect - 1
        left_reconstructed_drawing_rect = width_original_drawing_rect - 1
        width_reconstructed_drawing_rect = self.abscissa_dimension \
            - left_reconstructed_drawing_rect + 1
        height_reconstructed_drawing_rect = self.ordinate_dimension \
            - top_reconstructed_drawing_rect + 1

        reconstructed_drawing_rectangle = DrawingRectangle(self.screen,
                                                           left_reconstructed_drawing_rect,
                                                           top_reconstructed_drawing_rect, width_reconstructed_drawing_rect,
                                                           height_reconstructed_drawing_rect)

        original_drawing_rectangle.draw()
        reconstructed_drawing_rectangle.draw()

        return original_drawing_rectangle, reconstructed_drawing_rectangle

    def _constructed_top_right_rect(self):
        """Construit le rectangle qui se trouve en haut à droite"""

        top = 0
        left = self.original_drawing_rectangle.width
        width = self.screen.get_size()[0]\
            - self.original_drawing_rectangle.width
        height = self.original_drawing_rectangle.height

        top_right_rectangle = MyRectangle(self.screen,
                                          left, top, width, height)

        return top_right_rectangle

    def _constructed_bottom_left_rect(self):
        """Construit le rectangle qui se trouve en bas à gauche"""

        top = self.original_drawing_rectangle.height
        left = 0
        width = self.original_drawing_rectangle.width
        height = self.screen.get_size()[1]\
            - self.original_drawing_rectangle.height

        bottom_left_rectangle = MyRectangle(self.screen,
                                            left, top, width, height)

        return bottom_left_rectangle
