import pygame as pg
from drawElephantUtils import *

def initWindow():
	pg.init()

	screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
	#screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
	pg.display.set_caption("Title")

	background = pg.Surface(screen.get_size())
	background = background.convert()
	background.fill(BACKGROUND_COLOR)

	screen.blit(background, (0, 0))
	pg.display.flip()

	return screen

	
def clearScreen(screen):
	background = pg.Surface(screen.get_size())
	background = background.convert()
	background.fill(GRAY)

	screen.blit(background, (0, 0))