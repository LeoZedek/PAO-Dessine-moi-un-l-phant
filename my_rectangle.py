#!/usr/bin/env python3
"""Module proposant la classe abstraite MyRectangle"""

import pygame as pg
from draw_elephant_utils import BACKGROUND_COLOR

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
    def screen(self)->pg.Surface:
        """
        Renvoie la surface du rectangle
        """
        return self._screen

    def clear(self):
        """
        Vide le rectangle de tout dessins
        """
        pg.draw.rect(self.screen, BACKGROUND_COLOR, self)
        self.draw()
        pg.display.update()
