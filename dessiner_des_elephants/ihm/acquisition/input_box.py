#!/usr/bin/env python3
"""Module proposant la classe InputBox"""

import pygame as pg
from pygame_widgets.slider import Slider
from ..affichage.draw_elephant_utils import LABEL_HEIGHT, LABEL_WIDTH,\
    BLACK

from ..affichage.text_box import TextBox
from .virtual_keyboard import VirtualKeyboard


class InputBox(TextBox):
    '''
        Classe représentant une boite d'entrée dans laquelle, on peut mettre un nombre en entrée.
    '''

    def __init__(self, screen, left: int, top: int, width: int, height: int, label: str):

        super().__init__(screen, left, top, width, height)
        self._last_slider_value = -1
        self._value = None
        self._slider = None
        self._virtual_keyboard = VirtualKeyboard(self.screen)

        # Création du nom du rectangle qui sera affiché à gauche du rectangle
        letter_size_in_pixels = LABEL_HEIGHT * self.height * 0.5
        letter_size_in_points = round(letter_size_in_pixels * 72 / 96 * 1.5)

        font = pg.font.SysFont(None, letter_size_in_points)
        self._label = font.render(label, True, BLACK)
        text_width, text_height = font.size(label)

        x_display = self.left - LABEL_WIDTH * self.width \
            + (LABEL_WIDTH * self.width - text_width) / 2
        y_display = self.top + (self.height - text_height) / 2

        self._dimension_label_display = (x_display, y_display)

        self.screen.blit(self._label, self._dimension_label_display)

    @property
    def value(self) -> int:
        """
        Renvoie la valeur de la boite.
        """
        return self._value

    @value.setter
    def value(self, value: int):
        """
        Setter de la valeur dans la boite.
        """
        self._value = value

        if self.slider:
            if self.slider.min <= value <= self.slider.max:

                self.slider.setValue(value)
                self._last_slider_value = value

            elif value < self.slider.min:
                self.slider.setValue(self.slider.min)
                self._last_slider_value = self.slider.min

            else:
                self.slider.setValue(self.slider.max)
                self._last_slider_value = self.slider.max

    @property
    def slider(self) -> Slider:
        """
        Renvoie le slider de la boite.
        """
        return self._slider

    @slider.setter
    def slider(self, slider):
        """
        Setter du slider.
        """
        self._slider = slider
        if self._last_slider_value == -1:
            self.value = slider.getValue()
        self._last_slider_value = slider.getValue()

    def _update_slider_value(self) -> bool:
        """
        Méthode mettant à jour la valeur de la box si la valeur du slider à été touché.
        """
        slider_value = self.slider.getValue()

        if self._last_slider_value != slider_value:
            self._last_slider_value = slider_value
            self.value = slider_value
            return True

        return False

    def _update_text(self):
        if self.value is not None:
            self.set_text(str(self.value))

    def update(self) -> bool:
        """
        Méthode permettant de mettre à jour la valeur du slider s'il a bougé
        et le texte dans la boite.

        return : True si la valeur du slider à été modifié
                 False sinon
        """
        self.screen.blit(self._label, self._dimension_label_display)
        self._update_text()

        # Return True si la valeur du slider à été modifier
        return self._update_slider_value()

    def get_number_input(self) -> int:
        """
        Renvoie le nombre mis en entrée par l'utilisateur dans le clavier virtuel
        """

        self.value = self._virtual_keyboard.get_input_value()

        return self.value
