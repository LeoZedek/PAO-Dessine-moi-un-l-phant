#!/usr/bin/env python3
"""Module proposant la classe abstraite MyRectangle"""

import pygame as pg
from .draw_elephant_utils import BACKGROUND_COLOR, \
    DRAWING_RECT_BORDER_COLOR


class MyRectangle(pg.Rect):
    '''
    Classe représentant un rectangle, héritant de la class Rect de pygame.
    '''

    def __init__(self, screen, left: int, top: int, width: int, height: int):
        """
        screen: Surface sur lequelle le rectangle existe
        left : La coordonnée abscisse du coin haut gauche du rectangle
        top : La coordonnée ordonné du coin haut gauche du rectangle
        width : La largeur du rectangle
        height : La hauteur du rectangle
        """
        super().__init__(left, top, width, height)
        self._screen = screen

    @property
    def screen(self) -> pg.Surface:
        """
        Renvoie la surface du rectangle
        """
        return self._screen

    def clear(self):
        """
        Vide le rectangle de tout dessins
        """
        pg.draw.rect(self.screen, BACKGROUND_COLOR, self)

    def _draw_border(self, border_color=DRAWING_RECT_BORDER_COLOR):
        """
        Dessine les bordures du rectangle

        border_color : La couleur des bordures (tuples rgb)
        """
        pg.draw.line(self.screen, border_color,
                     (self.left, self.top), (self.left + self.width - 1, self.top))

        pg.draw.line(self.screen, border_color,
                     (self.left, self.top), (self.left, self.top + self.height - 1))

        pg.draw.line(self.screen, border_color,
                     (self.left + self.width - 1, self.top),
                     (self.left + self.width - 1, self.top + self.height - 1))

        pg.draw.line(self.screen, border_color,
                     (self.left, self.top + self.height - 1),
                     (self.left + self.width - 1, self.top + self.height - 1))
