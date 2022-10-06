#!/usr/bin/env python3
"""Module proposant la classe DrawingRectangle"""

import pygame as pg
from draw_elephant_utils import DRAWING_RECT_BORDER_COLOR
from draw_elephant_utils import POINT_RADIUS, COLOR_LINE
from my_rectangle import MyRectangle

class DrawingRectangle(MyRectangle):
    '''
        Classe représentant un rectangle dans lequelle on peut dessiner une figure.
    '''

    def draw(self):
        """
        Dessine les bordures du rectangle.
        """
        self._draw_border()
        pg.display.update()

    def _draw_point(self, point):
        """
        Méthode privée
        """

        x_dimension, y_dimension = self.screen.get_size()

        x_point = point.abscisse + (x_dimension // 2)
        y_point = -point.ordonnee + (y_dimension // 2)

        x_ratio = self.width / x_dimension
        y_ratio = self.height / y_dimension

        new_x = x_point * x_ratio + self.left
        new_y = y_point * y_ratio + self.top

        pg.draw.circle(self.screen, COLOR_LINE, (new_x, new_y), POINT_RADIUS)

    def draw_points(self, points):
        """
        Dessine la liste de point dans le rectangle.
        """
        for point in points:
            self._draw_point(point)

        pg.display.update()

    def _draw_border(self):
        """
        Fonction privée
        """
        pg.draw.line(self.screen, DRAWING_RECT_BORDER_COLOR,\
         (self.left, self.top), (self.left + self.width -1, self.top))

        pg.draw.line(self.screen, DRAWING_RECT_BORDER_COLOR,\
         (self.left, self.top), (self.left, self.top + self.height -1))

        pg.draw.line(self.screen, DRAWING_RECT_BORDER_COLOR,\
         (self.left + self.width - 1, self.top),\
          (self.left + self.width - 1, self.top + self.height - 1))

        pg.draw.line(self.screen, DRAWING_RECT_BORDER_COLOR,\
         (self.left, self.top + self.height - 1),\
          (self.left + self.width - 1, self.top + self.height - 1))
