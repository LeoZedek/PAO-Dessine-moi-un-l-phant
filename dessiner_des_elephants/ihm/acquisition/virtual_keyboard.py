#!/usr/bin/env python3
"""Module proposant la classe VirtualKeyboard"""

import pygame as pg
from pygame_widgets.button import Button
from ..affichage.draw_elephant_utils import PROPORTION_VIRTUAL_KEYBOARD_HEIGHT,\
                                            BLACK

KEY_PARAMETERS = {
    "imageHAlign" : 'centre',
    "imageVAlign" : 'centre',
    "borderThickness" : 3,
    "borderColor" : BLACK,
    "fontSize" : 40
}

def _remove_last_letter_from_string(string):

    if len(string) == 0:
        return string

    temp_list_char = list(string)
    temp_list_char.pop()

    return "".join(temp_list_char)

class VirtualKeyboard():
    """
        Class représentant la classe clavier virtuel.
    """
    def __init__(self, screen):
        self._screen = screen

        self._height = round(self._screen.get_size()[1] * PROPORTION_VIRTUAL_KEYBOARD_HEIGHT)
        self._top = self._height // 2

        self._key_padding = (self._height * 1/5) // 3
        # Key is a square
        self._key_dimension = (self._height * 4/5) // 4

        self._width = 2 * self._key_padding + 3 * self._key_dimension

        self._left = (self._screen.get_size()[0] - self._width) // 2

        self._keys = {}

        self._string_value = ""

    @property
    def screen(self)->pg.Surface:
        """Getter de l'objet Surface du clavier"""
        return self._screen

    @property
    def height(self)->int:
        """Getter de la hauteur du clavier"""
        return self._height

    @property
    def width(self)->int:
        """Getter de la largeur du clavier"""
        return self._width

    @property
    def key_padding(self)->int:
        """Getter de la marge entre les touches du clavier"""
        return self._key_padding

    @property
    def key_dimension(self)->int:
        """Getter de la dimension des touches.
        Les touches étant carrés, cela correspond donc à la hauteur et la largeur des touches."""
        return self._key_dimension

    @property
    def top(self)->int:
        """Getter de l'ordonnée du coin gauche du clavier virtuel"""
        return self._top

    @property
    def left(self)->int:
        """Getter de l'abscisse du coin gauche du clavier virtuel"""
        return self._left

    def _add_key_by_tag(self, key, key_tag):
        self._keys[key_tag] = key

    def _add_character_to_string_value(self, charactere):
        if len(self._string_value) < 4 and len(charactere) == 1:
            self._string_value += charactere

    def _return_press(self):
        self._string_value = _remove_last_letter_from_string(self._string_value)

    def _create_number_keys(self):
        button_parameters = KEY_PARAMETERS.copy()
        button_parameters["text"] = "<-"
        button_parameters["onRelease"] = self._return_press

        button_return = Button(self.screen,
                               x = self.left, width = self.key_dimension, \
                               y = self.top + 3 * self.key_dimension + 3 * self.key_padding,\
                               height = self.key_dimension, **button_parameters)

        self._add_key_by_tag(button_return, "return")

        button_parameters = KEY_PARAMETERS.copy()
        button_parameters["text"] = "0"
        button_parameters["onRelease"] = lambda : self._add_character_to_string_value("0")

        zero_button = Button(self.screen,
                               x = self.left + self.key_dimension + self.key_padding,\
                               y = self.top + 3 * self.key_dimension + 3 * self.key_padding,\
                               width = self.key_dimension, height = self.key_dimension,\
                               **button_parameters)

        self._add_key_by_tag(zero_button, "0")

        button_parameters = KEY_PARAMETERS.copy()
        button_parameters["text"] = "OK"
        button_parameters["onRelease"] = lambda : print("temp")

        enter_button = Button(self.screen,
                               x = self.left + 2 * self.key_dimension + 2 * self.key_padding,\
                               y = self.top + 3 * self.key_dimension + 3 * self.key_padding,\
                               width = self.key_dimension, height = self.key_dimension,\
                               **button_parameters)

        self._add_key_by_tag(enter_button, "enter")

        for number in range(1, 10):

            button_parameters = KEY_PARAMETERS.copy()
            button_parameters["text"] = str(number)
            button_parameters["onRelease"] = lambda : self._add_character_to_string_value(str(number))

            button = Button(self.screen,
                            x = self.left + (2 - (number - 1) % 3) * (self.key_dimension + self.key_padding),\
                            y = self.top + (2 - (number - 1) // 3 ) * (self.key_dimension + self.key_padding),\
                            width = self.key_dimension, height = self.key_dimension,\
                            **button_parameters)

            self._add_key_by_tag(button, str(number))