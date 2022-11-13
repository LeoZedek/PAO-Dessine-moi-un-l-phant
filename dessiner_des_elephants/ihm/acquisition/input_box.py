#!/usr/bin/env python3
"""Module proposant la classe InputBox"""

import pygame as pg
from pygame_widgets.slider import Slider
from ..affichage.draw_elephant_utils import BOX_BORDER_COLOR_ON_FOCUS
from ..affichage.text_box import TextBox

# Function to verify that the pressed key is a digit
# Private function
def _is_digit_key(key):
    return key in range(pg.K_0, pg.K_9 + 1)

def _remove_last_letter_from_string(string):

    if len(string) == 0:
        return string

    temp_list_char = list(string)
    temp_list_char.pop()

    return "".join(temp_list_char)

class InputBox(TextBox):
    '''
        Classe représentant une boite d'entrée dans laquelle, on peut mettre un nombre en entrée.
    '''

    def __init__(self, screen, left: int, top: int, width: int, height: int):

        super().__init__(screen, left, top, width, height)
        self._last_slider_value = -1
        self._value = None
        self._slider = None

    @property
    def value(self)->int:
        """
        Renvoie la valeur de la boite.
        """
        return self._value

    @value.setter
    def value(self, value : int):
        """
        Setter de la valeur dans la boite.
        """
        self._value = value

    @property
    def slider(self)->Slider:
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

    def _update_slider_value(self):
        """
        Méthode mettant à jour la valeur de la box si la valeur du slider à été touché.
        """
        slider_value = self.slider.getValue()

        if self._last_slider_value != slider_value:
            self._last_slider_value = slider_value
            self.value = slider_value

    def _update_text(self):
        if self.value is not None:
            self.set_text(str(self.value))

    def update(self):
        """
        Méthode permettant de mettre à jour la valeur du slider s'il a bougé
        et le texte dans la boite.
        """
        self._update_text()
        self._update_slider_value()

    def get_number_input(self)->int:
        """
        Renvoie le nombre mis en entrée par l'utilisateur

        Appuyer sur Entrée pour envoyer la valeur
        """

        self.clear()
        self.draw(BOX_BORDER_COLOR_ON_FOCUS)
        pg.display.update(self)

        not_done = True

        my_number = ""

        while not_done:
            for event in pg.event.get():

                if event.type == pg.KEYDOWN:
                    if _is_digit_key(event.key) and len(my_number) < 4:
                        my_number += event.unicode
                        self.set_text(my_number, BOX_BORDER_COLOR_ON_FOCUS)

                    if event.key == pg.K_RETURN:
                        if len(my_number) > 0:
                            not_done = False

                    if event.key == pg.K_BACKSPACE:
                        if len(my_number) > 0:
                            my_number = _remove_last_letter_from_string(my_number)
                            self.set_text(my_number, BOX_BORDER_COLOR_ON_FOCUS)

        self._value = int(my_number)

        return int(my_number)
