#!/usr/bin/env python3
"""Module proposant la classe DrawingRectangle"""

from math import pi
import time
import pygame as pg
from decomposition_en_serie_de_fourier import decompositions_en_serie_de_fourier
from dessiner_des_elphants.ihm.affichage.draw_elephant_utils import POINT_RADIUS, COLOR_LINE
from dessiner_des_elphants.ihm.affichage.draw_elephant_utils import DRAWING_RECT_BORDER_COLOR
from dessiner_des_elphants.ihm.affichage.my_rectangle import MyRectangle
from .screen_utils import clear_screen
from dessiner_des_elphants.logique_metier.series_de_cercles import SeriesCercles
from dessiner_des_elphants.logique_metier.points.point import Point2D

class DrawingRectangle(MyRectangle):
    '''
        Classe représentant un rectangle dans lequelle on peut dessiner une figure.
    '''

    def draw(self):
        """
        Dessine les bordures du rectangle.
        """
        self._draw_border(DRAWING_RECT_BORDER_COLOR)
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

            points : une liste de Point2D
        """
        for point in points:
            self._draw_point(point)

        pg.display.update()

    def draw_reconstructed_drawing(self, original_drawing_rectangle, points, number_circle):
        """
        Commence la reconstruction des cercles et garde les points dessiner dans
        le rectangle du dessin original.
        Précondition : le rapport hauteur/largueur du DrawingRectangle
                       doit être le même que celui de la fenêtre.

            original_drawing_rectangle : le DrawingRectangle qui contiendra le dessin original
            points : la liste de Point2D du dessin original
            number_circle : le nombre de cercle utilisé pour reconstruire le dessin
        """

        points_complexe = [complex(point) for point in points]

        coeff_cn = decompositions_en_serie_de_fourier(points_complexe, number_circle)

        center_drawing = Point2D(self.centerx,\
            self.centery)
        pas = 2*pi/1024
        scale = self.height / self.screen.get_size()[1]

        my_circles_serie = SeriesCercles(center_drawing, coeff_cn,\
            scale, pas, self.screen)

        not_done = True

        while not_done:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    not_done = False

                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_q:
                        not_done = False

            clear_screen(self.screen)

            my_circles_serie.dessiner_le_chemin()
            my_circles_serie.dessiner_les_cercles()
            original_drawing_rectangle.draw_points(points)
            original_drawing_rectangle.draw()
            self.draw()

            if my_circles_serie.have_done_complete_tour():
                not_done = False

            pg.display.update()

            time.sleep(0.01)
