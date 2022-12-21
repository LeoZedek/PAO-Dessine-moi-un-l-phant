#!/usr/bin/env python3
"""Module proposant les fonctions pour gérer la fenêtre d'affichage"""

import pygame as pg
from .draw_elephant_utils import BACKGROUND_COLOR


def init_window() -> pg.Surface:
    '''Fonction permettant l\'initialisation de la fenêtre

    return l'objet pg.Surface
    '''
    pg.init()

    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    pg.display.set_caption("Title")

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)

    screen.blit(background, (0, 0))
    pg.display.flip()

    return screen


def clear_screen(screen: pg.Surface):
    '''Fonction qui vide la fenêtre de tout dessin

    screen : l'objet pg.Surface qui sera rénitialisé
    '''

    screen.fill(BACKGROUND_COLOR)

    # background = pg.Surface(screen.get_size())
    # background = background.convert()
    # background.fill(BACKGROUND_COLOR)

    # screen.blit(background, (0, 0))
