#!/usr/bin/env python3
"""Module proposant la classe InputBox"""

import pygame as pg
from dessiner_des_elphants.ihm.affichage.draw_elephant_utils import BLACK, BOX_BORDER_WIDTH, BOX_BORDER_COLOR
from dessiner_des_elphants.ihm.affichage.draw_elephant_utils import BOX_BORDER_COLOR_ON_FOCUS
from dessiner_des_elphants.ihm.affichage.my_rectangle import MyRectangle

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

    else:

        temp_list_char = list(string)
        temp_list_char.pop()

        return "".join(temp_list_char)

class InputBox(MyRectangle):
    '''
        Classe représentant une boite d'entrée dans laquelle, on peut mettre un nombre en entrée.
    '''

    def draw(self, border_color = BOX_BORDER_COLOR):
        """Dessine le rectangle"""
        pg.draw.rect(self.screen, border_color, self, width = BOX_BORDER_WIDTH)
        pg.display.update()

    def set_text(self, text, border_color = BOX_BORDER_COLOR):
        """
        Dessine le text dans le rectangle

            text : Le texte qui va être afficher dans le rectangle
        """
        self.clear()
        self.draw(border_color)

        letter_size_in_pixels = self.height * 0.8
        letter_size_in_points = round(letter_size_in_pixels * 72 / 96  * 1.5)

        font = pg.font.SysFont(None, letter_size_in_points)
        text_to_display = font.render(text, True, BLACK)
        text_width, text_height = font.size(text)

        x_display = self.left + (self.width - text_width) / 2
        y_display = self.top + (self.height - text_height) / 2

        self.screen.blit(text_to_display, (x_display, y_display))
        pg.display.update()

    def get_number_input(self)->int:
        """
        Renvoie le nombre mis en entrée par l'utilisateur

        Appuyer sur Entrée pour envoyer la valeur
        """

        self.clear()
        self.draw(BOX_BORDER_COLOR_ON_FOCUS)

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
