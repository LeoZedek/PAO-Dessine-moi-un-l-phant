#!/usr/bin/env python3
"""Module proposant les fonctions qui créer les sliders"""
import pygame as pg

from pygame_widgets.slider import Slider

from dessiner_des_elephants.ihm.affichage.constructed_rectangles import ConstructedRectangles
from dessiner_des_elephants.ihm.affichage.draw_elephant_utils import SLIDER_COLOR,\
    SLIDER_HANDLE_COLOR, \
    MIN_CIRCLE_SLIDER_VALUE,\
    MAX_CIRCLE_SLIDER_VALUE,\
    CIRCLE_SLIDER_STEP,\
    MIN_POINTS_SLIDER_VALUE,\
    MAX_POINTS_SLIDER_VALUE,\
    POINTS_SLIDER_STEP,\
    PROPORTION_PARAMETERS_BUTTON
from dessiner_des_elephants.logique_metier.point import Point2D


def create_sampling_slider(screen: pg.Surface,
                           constructed_rectangle: ConstructedRectangles,
                           points: list[Point2D]):
    """
      Créer le slider pour le nombre de points

      screen : Surface sur laquel l'utilisateur va utiliser le slider
      constructed_rectangle : l'objet constructed_rectangle qui contient tous les rectangles
      points : list de Point2D, utile pour changer le min ou le max du slider si besoin

      return : le slider pour choisir le nombre de points échantillonés
    """

    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    sampling_box = constructed_rectangle.sampling_box
    number_circle_box = constructed_rectangle.number_circle_box

    width_slider = (screen.get_size()[0] - constructed_rectangle._input_box_width) \
        * PROPORTION_PARAMETERS_BUTTON
    height_slider = number_circle_box.top - sampling_box.top \
        - sampling_box.height - constructed_rectangle.box_padding_ordinate

    left_slider_sampling = original_drawing_rectangle.width * 1.05
    top_slider_sampling = sampling_box.top + sampling_box.height \
        + (constructed_rectangle.box_padding_ordinate // 2)

    min_sampling = min(len(points), MIN_POINTS_SLIDER_VALUE)
    max_sampling = len(points)

    slider_sampling = Slider(screen, left_slider_sampling, top_slider_sampling,
                             width_slider, height_slider,
                             min=min_sampling, max=max_sampling,
                             step=POINTS_SLIDER_STEP,
                             handleColour=SLIDER_HANDLE_COLOR, colour=SLIDER_COLOR)
    return slider_sampling


def create_number_circle_slider(screen: pg.Surface,
                                constructed_rectangle: ConstructedRectangles):
    """
      Créer le slider pour le nombre de cercle

      screen : Surface sur laquel l'utilisateur va utiliser le slider
      constructed_rectangle : l'objet constructed_rectangle qui contient toutes les boites

      return : le slider pour choisir le nombre de cercle
    """

    original_drawing_rectangle = constructed_rectangle.original_drawing_rectangle
    sampling_box = constructed_rectangle.sampling_box
    number_circle_box = constructed_rectangle.number_circle_box

    width_slider = (screen.get_size()[0] - constructed_rectangle._input_box_width) \
        * PROPORTION_PARAMETERS_BUTTON
    height_slider = number_circle_box.top - sampling_box.top \
        - sampling_box.height - constructed_rectangle.box_padding_ordinate

    left_slider_number_circle = original_drawing_rectangle.width * 1.05
    top_slider_number_circle = number_circle_box.top + number_circle_box.height \
        + (constructed_rectangle.box_padding_ordinate // 2)

    slider_number_circle = Slider(screen, left_slider_number_circle,
                                  top_slider_number_circle, width_slider, height_slider,
                                  min=MIN_CIRCLE_SLIDER_VALUE,
                                  max=MAX_CIRCLE_SLIDER_VALUE,
                                  step=CIRCLE_SLIDER_STEP,
                                  handleColour=SLIDER_HANDLE_COLOR, colour=SLIDER_COLOR)
    return slider_number_circle
