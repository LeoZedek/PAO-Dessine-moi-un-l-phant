#!/usr/bin/env python3
"""Module proposant la classe DrawingRectangle"""

from math import pi
import time
import pygame as pg
from ...logique_metier.decomposition_en_serie_de_fourier import decompositions_en_serie_de_fourier
from .draw_elephant_utils import POINT_RADIUS, COLOR_LINE
from .draw_elephant_utils import DRAWING_RECT_BORDER_COLOR
from .my_rectangle import MyRectangle
from .screen_utils import clear_screen
from ...logique_metier.series_cercles import SeriesCercles
from ...logique_metier.point import Point2D
from .dessiner_series_cercles import dessiner_series_cercles


class DrawingRectangle(MyRectangle):
    '''
        Classe représentant un rectangle dans lequelle on peut dessiner une figure.
    '''

    def draw(self):
        """
        Dessine les bordures du rectangle.
        """
        self._draw_border(DRAWING_RECT_BORDER_COLOR)


    def calcul_points(self, point1: Point2D, point2: Point2D):
        """
        calcule les cordonnées des deux points servant à construire la droite pour l'affichage
        """
        x_dimension, y_dimension = self.screen.get_size()

        x_ratio = self.width / x_dimension
        y_ratio = self.height / y_dimension

        x_point1 = point1.abscisse + (x_dimension // 2)
        y_point1 = -point1.ordonnee + (y_dimension // 2)

        x_point2 = point2.abscisse + (x_dimension // 2)
        y_point2 = -point2.ordonnee + (y_dimension // 2)

        new_x1 = x_point1 * x_ratio + self.left
        new_y1 = y_point1 * y_ratio + self.top

        new_x2 = x_point2 * x_ratio + self.left
        new_y2 = y_point2 * y_ratio + self.top

        return new_x1, new_y1, new_x2, new_y2


    def draw_points(self, points: list) -> None:
        """
        dessine la figure originale avec le sampling choisi
            points : la liste de Point2D du dessin original
        """
        for i in range(len(points)):
            if(i == len(points)-1):
                x1, y1, x2, y2 = self.calcul_points(points[i], points[0])
            else:
                x1, y1, x2, y2 = self.calcul_points(points[i], points[i+1])
            pg.draw.line(self.screen, COLOR_LINE, (x1, y1), (x2,y2), 3)   



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

        coeff_cn = decompositions_en_serie_de_fourier(
            points_complexe, number_circle)

        center_drawing = Point2D(self.centerx,
                                 self.centery)
        pas = 2*pi/1024
        scale = self.height / self.screen.get_size()[1]

        my_circles_serie = SeriesCercles(center_drawing, coeff_cn,
                                         scale, pas)

        not_done = True

        while not_done:

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    not_done = False

                if event.type == pg.MOUSEBUTTONDOWN:
                    not_done = False

            clear_screen(self.screen)

            dessiner_series_cercles(
                series_cercles=my_circles_serie, screen=self.screen)
            self.draw()

            if my_circles_serie.have_done_complete_tour():
                not_done = False

            pg.display.update(self)

            time.sleep(0.01)

        return my_circles_serie.chemin
