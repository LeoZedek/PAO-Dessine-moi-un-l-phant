#!/usr/bin/env python3
"""Module proposant la classe InputBox"""

import pygame as pg
from .draw_elephant_utils import BLACK, BOX_BORDER_WIDTH, BOX_BORDER_COLOR
from .my_rectangle import MyRectangle

class TextBox(MyRectangle):
    '''
        Classe représentant une boite dans laquelle on peut mettre un text dedans.
    '''

    def draw(self, border_color = BOX_BORDER_COLOR):
        """Dessine le rectangle"""
        pg.draw.rect(self.screen, border_color, self, width = BOX_BORDER_WIDTH)

    def set_text(self, text, border_color = BOX_BORDER_COLOR):
        """
        Dessine le text dans le rectangle

            text : Le texte qui va être afficher dans le rectangle
        """
        self.clear()
        self.draw(border_color)

        letter_size_in_pixels = self.height * 0.7
        letter_size_in_points = round(letter_size_in_pixels * 72 / 96  * 1.5)

        font = pg.font.SysFont(None, letter_size_in_points)
        text_to_display = font.render(text, True, BLACK)
        text_width, text_height = font.size(text)

        x_display = self.left + (self.width - text_width) / 2
        y_display = self.top + (self.height - text_height) / 2

        self.screen.blit(text_to_display, (x_display, y_display))
        pg.display.update(self)
