#!/usr/bin/env python3
"""Module proposant la classe InputBox"""

import pygame as pg
from pygame_widgets.slider import Slider
from ..affichage.draw_elephant_utils import BOX_BORDER_COLOR_ON_FOCUS, BOX_BORDER_COLOR, \
                                            SLIDER_HANDLE_COLOR, SLIDER_COLOR
from ..affichage.text_box import TextBox

# Function to verify that the pressed key is a digit
# Private function
def _is_digit_key(key):
    """
    Fonction privée
	"""
    return key in range(pg.K_0, pg.K_9 + 1)

def _remove_last_letter_from_string(string):
    """
    Fonction privée
    """

    if len(string) == 0:
        return string

    temp_list_char = list(string)
    temp_list_char.pop()

    return "".join(temp_list_char)

class InputBox(TextBox):
    '''
        Classe représentant une boite d'entrée dans laquelle, on peut mettre un nombre en entrée.
    '''

    def __init__(self, screen, left: int, top: int, width: int, height: int, **kwargs):

        super().__init__(screen, left, top, width, height)
        #self.slider = self._create_slider(kwargs.get("min_value"),\
        #                                  kwargs.get("max_value"),\
        #                                  kwargs.get("step"))

    def _create_slider(self, min_value, max_value, step):

        width_slider = self.width
        height_slider = self.height // 3

        left_slider = self.left
        top_slider = self.top + self.height \
                     + (self.height // 4)

        slider = Slider(self.screen, left_slider, top_slider, \
                                 width_slider, height_slider, \
                                 min = min_value, max = max_value, \
                                 step = step, \
                                 handleColour = SLIDER_HANDLE_COLOR, colour = SLIDER_COLOR)
        return slider

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

        self.set_text(my_number)

        return int(my_number)
