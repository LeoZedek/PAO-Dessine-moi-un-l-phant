#!/usr/bin/env python3
"""
Module contenant la class MySlider.
"""

from pygame_widgets.slider import Slider
from ..affichage.draw_elephant_utils import SLIDER_COLOR, SLIDER_HANDLE_COLOR

class MySlider(Slider):
    """
    Classe représentant nos slider.
    """

    def __init__(self, left, top, width, height):
        """
            left : les coordonné abscisse
            top : les coordonné ordonné
            width : la largeur du slider
            height : la hauteur du slider

        """

        super().__init__(left, top, width, height, \
            colour = SLIDER_COLOR, handleColour = SLIDER_HANDLE_COLOR)
