#!/usr/bin/env python3
"""Module permettant de construire les différents rectangle"""

from .draw_elephant_utils import INPUT_SAMPLING_BOX_WIDTH
from .draw_elephant_utils import INPUT_SAMPLING_BOX_PADDING_RIGHT, INPUT_SAMPLING_BOX_PADDING_TOP
from .draw_elephant_utils import INPUT_SAMPLING_BOX_HEIGHT
from ..acquisition.clavier.input_box import InputBox
from .constructed_drawing_rectangle import ConstructedDrawingRectangle

class ConstructedRectangles(ConstructedDrawingRectangle):
    """
    Classe permettant de construire les differents rectangle de l'ihm.
    Elle permet de construire les deux rectangles de dessins et les 3 rectangles d'input
    """

    def __init__(self, screen):

        super().__init__(screen)

        self._box_width, self._box_height = self._constructed_box_abscissa_dimension()

        self._box_padding_abscissa, self._box_padding_ordinate = \
            self._constructed_box_padding()

        self._sampling_box = self._constructed_sampling_box()

        self._number_circle_box = self._constructed_number_circle_box()

        self._start_box = self._constructed_start_box()

    @property
    def box_width(self)->int:
        """
        Getter pour obtenir la largeur des boites.
        """
        return self._box_width

    @property
    def box_height(self)->int:
        """
        Getter pour obtenir la hauteur des boites.
        """
        return self._box_height

    @property
    def box_padding_abscissa(self)->int:
        """
        Getter pour obtenir la marge sur l'abscisse des boites.
        """
        return self._box_padding_abscissa

    @property
    def box_padding_ordinate(self)->int:
        """
        Getter pour obtenir la marge sur l'ordonnée des boites.
        """
        return self._box_padding_ordinate

    @property
    def sampling_box(self):
        """
        Getter pour obtenir la boite d'entrée pour le nombre d'échantillonage.
        """
        return self._sampling_box

    @property
    def number_circle_box(self):
        """
        Getter pour obtenir la boite d'entrée pour le nombre de cercle.
        """
        return self._number_circle_box

    @property
    def start_box(self):
        """
        Getter pour obtenir la boite d'entrée pour commencer le dessin.
        """
        return self._start_box

    def _constructed_box_abscissa_dimension(self):
        """
        Fonction privée
        """
        box_height = round(INPUT_SAMPLING_BOX_HEIGHT * self.original_drawing_rectangle.height)
        box_width = round(INPUT_SAMPLING_BOX_WIDTH * self.original_drawing_rectangle.width)

        return box_width, box_height

    def _constructed_box_padding(self):
        """
        Fonction privée
        """
        padding_abscissa_box = round(self.original_drawing_rectangle.width \
            * INPUT_SAMPLING_BOX_PADDING_RIGHT)
        padding_ordinate_box = round(self.original_drawing_rectangle.height \
            * INPUT_SAMPLING_BOX_PADDING_TOP)

        return padding_abscissa_box, padding_ordinate_box

    def _constructed_sampling_box(self):
        """
        Fonction privée
        """
        top_sampling_box = self.box_padding_ordinate
        left_sampling_box = self.box_padding_abscissa + self.original_drawing_rectangle.width
        height_sampling_box = self.box_height
        width_sampling_box = self.box_width

        sampling_box = InputBox(self.screen, left_sampling_box, \
            top_sampling_box, width_sampling_box, height_sampling_box)
        sampling_box.draw()

        return sampling_box

    def _constructed_number_circle_box(self):
        """
        Fonction privée
        """
        height_number_circle_box = self.box_height
        width_number_circle_box = self.box_width
        top_number_circle_box = self.reconstructed_drawing_rectangle.top \
            - self.box_padding_ordinate - self.box_height

        left_number_circle_box = self.abscissa_dimension \
        - self.box_padding_abscissa - self.box_width

        number_circle_box = InputBox(self.screen, left_number_circle_box, \
            top_number_circle_box, width_number_circle_box, height_number_circle_box)
        number_circle_box.draw()

        return number_circle_box

    def _constructed_start_box(self):
        """
        Fonction privée
        """
        height_start_box = self.box_height
        width_start_box = self.box_width
        top_start_box = self.reconstructed_drawing_rectangle.top \
            + self.reconstructed_drawing_rectangle.height // 2 - height_start_box // 2
        left_start_box = self.abscissa_dimension - self.box_padding_abscissa - self.box_width

        start_box = InputBox(self.screen, left_start_box, \
            top_start_box, width_start_box, height_start_box)
        start_box.draw()
        start_box.set_text("GO !")

        return start_box
