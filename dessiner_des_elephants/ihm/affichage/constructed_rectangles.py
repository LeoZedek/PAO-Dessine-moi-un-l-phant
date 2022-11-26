#!/usr/bin/env python3
"""Module permettant de construire les différents rectangle"""

from .draw_elephant_utils import INPUT_SAMPLING_BOX_WIDTH
from .draw_elephant_utils import INPUT_SAMPLING_BOX_PADDING_RIGHT, INPUT_SAMPLING_BOX_PADDING_TOP
from .draw_elephant_utils import INPUT_SAMPLING_BOX_HEIGHT, LABEL_WIDTH
from ..acquisition.input_box import InputBox
from .text_box import TextBox
from .constructed_drawing_rectangle import ConstructedDrawingRectangle

class _BoxDimension():

    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self)->int:
        """
        Getter pour obtenir la largeur
        """

        return self._width

    @property
    def height(self)->int:
        """
        Getter pour obtenir la longueur
        """

        return self._height

class _BoxPadding():

    def __init__(self, padding_abscissa, padding_ordinate):
        self._padding_abscissa = padding_abscissa
        self._padding_ordinate = padding_ordinate

    @property
    def padding_abscissa(self)->int:
        """
        Getter du padding des abscisses
        """

        return self._padding_abscissa

    @property
    def padding_ordinate(self)->int:
        """
        Getter du padding des ordonnés
        """

        return self._padding_ordinate

class ConstructedRectangles(ConstructedDrawingRectangle):
    """
    Classe permettant de construire les differents rectangle de l'ihm.
    Elle permet de construire les deux rectangles de dessins et les 3 rectangles d'input
    """

    def __init__(self, screen):

        super().__init__(screen)

        self._box_dimension = self._constructed_box_dimension()

        self._box_padding = self._constructed_box_padding()

        self._box_map = {}

        self._add_box(self._constructed_sampling_box(), "sampling_box")
        self._add_box(self._constructed_number_circle_box(), "number_circle_box")
        self._add_box(self._constructed_start_box(), "start_box")
        self._add_box(self._constructed_draw_box(), "draw_box")
        self._add_box(self._constructed_redraw_box(), "redraw_box")
        self._add_box(self._constructed_quit_box(), "quit_box")

    def _add_box(self, box, box_tag):
        self._box_map[box_tag] = box

    def _get_box_by_tag(self, box_tag):
        return self._box_map[box_tag]

    @property
    def box_width(self)->int:
        """
        Getter pour obtenir la largeur des boites.
        """
        return self._box_dimension.width

    @property
    def box_height(self)->int:
        """
        Getter pour obtenir la hauteur des boites.
        """
        return self._box_dimension.height

    @property
    def box_padding_abscissa(self)->int:
        """
        Getter pour obtenir la marge sur l'abscisse des boites.
        """
        return self._box_padding.padding_abscissa

    @property
    def box_padding_ordinate(self)->int:
        """
        Getter pour obtenir la marge sur l'ordonnée des boites.
        """
        return self._box_padding.padding_ordinate

    @property
    def sampling_box(self):
        """
        Getter pour obtenir la boite d'entrée pour le nombre d'échantillonage.
        """
        return self._get_box_by_tag("sampling_box")

    @property
    def number_circle_box(self):
        """
        Getter pour obtenir la boite d'entrée pour le nombre de cercle.
        """
        return self._get_box_by_tag("number_circle_box")

    @property
    def start_box(self):
        """
        Getter pour obtenir la boite d'entrée pour commencer le dessin.
        """
        return self._get_box_by_tag("start_box")

    @property
    def draw_box(self):
        """
        Getter pour obtenir la boite d'entrée pour recommencer la reconstruction du dessin.
        """
        return self._get_box_by_tag("draw_box")

    @property
    def redraw_box(self):
        """
        Getter pour obtenir la boite d'entrée pour redessiner un dessin.
        """
        return self._get_box_by_tag("redraw_box")

    @property
    def quit_box(self):
        """
        Getter pour obtenir la boite de sortie pour quitter le programme.
        """
        return self._get_box_by_tag("quit_box")

    def _constructed_box_dimension(self):
        """
        Fonction privée
        """
        box_height = round(INPUT_SAMPLING_BOX_HEIGHT * self.original_drawing_rectangle.height)
        box_width = round(INPUT_SAMPLING_BOX_WIDTH * self.original_drawing_rectangle.width)

        return _BoxDimension(box_width, box_height)

    def _constructed_box_padding(self):
        """
        Fonction privée
        """
        padding_abscissa_box = round(self.original_drawing_rectangle.width \
            * INPUT_SAMPLING_BOX_PADDING_RIGHT)
        padding_ordinate_box = round(self.original_drawing_rectangle.height \
            * INPUT_SAMPLING_BOX_PADDING_TOP)

        return _BoxPadding(padding_abscissa_box, padding_ordinate_box)

    def _constructed_sampling_box(self):
        """
        Fonction privée
        """
        top_sampling_box = self.box_padding_ordinate
        left_sampling_box = self.original_drawing_rectangle.width\
                            + LABEL_WIDTH * self.box_width
        height_sampling_box = self.box_height
        width_sampling_box = self.box_width

        sampling_box = InputBox(self.screen, left_sampling_box, \
            top_sampling_box, width_sampling_box, height_sampling_box,\
            "number points :")

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
            top_number_circle_box, width_number_circle_box, height_number_circle_box,\
            "number circle :")

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

        start_box = TextBox(self.screen, left_start_box, \
            top_start_box, width_start_box, height_start_box)

        return start_box

    def _constructed_draw_box(self):

        height_box = self.box_height
        width_box = 2 * self.box_width
        top_box = self.box_padding_ordinate
        left_box = self.screen.get_size()[0]\
            - self.box_padding_abscissa\
            - width_box

        draw_box = TextBox(self.screen, left_box, top_box, \
            width_box, height_box)

        return draw_box

    def _constructed_redraw_box(self):

        height_box = self.box_height
        width_box = 2 * self.box_width
        top_box = self.box_padding_ordinate * 2 + self.draw_box.height
        left_box = self.screen.get_size()[0]\
            - self.box_padding_abscissa\
            - width_box

        redraw_box = TextBox(self.screen, left_box, top_box, \
            width_box, height_box)

        return redraw_box

    def _constructed_quit_box(self):
        """
        Fonction privée
        """
        height_start_box = self.box_height
        width_start_box = self.box_width
        top_start_box = self.reconstructed_drawing_rectangle.top \
            + self.reconstructed_drawing_rectangle.height // 2 - height_start_box // 2
        left_start_box = self.abscissa_dimension - self.box_padding_abscissa - self.box_width

        quit_box = TextBox(self.screen, left_start_box, \
            top_start_box, width_start_box, height_start_box)

        return quit_box
