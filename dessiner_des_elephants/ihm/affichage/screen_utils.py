#!/usr/bin/env python3
"""Module proposant les fonctions pour gérer la fenêtre d'affichage"""

import pygame as pg
from .draw_elephant_utils import BACKGROUND_COLOR

def init_window()->pg.Surface:
    '''Fonction permettant l\'initialisation de la fenêtre'''
    pg.init()

    screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
    pg.display.set_caption("Title")

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)

    screen.blit(background, (0, 0))
    pg.display.flip()

    return screen

def clear_screen(screen):
    '''Fonction qui vide la fenêtre de tout dessin'''

    background = pg.Surface(screen.get_size())
    background = background.convert()
    background.fill(BACKGROUND_COLOR)

    screen.blit(background, (0, 0))
