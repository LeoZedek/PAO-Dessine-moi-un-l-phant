import pygame as pg
from drawElephantUtils import BLACK, BACKGROUND_COLOR, DRAWING_RECT_BORDER_COLOR, DRAWING_RECT_BORDER_WIDTH

class MyRectangle(pg.Rect):
	'''
		Classe représentant un rectangle, héritant de la class Rect de pygame.
	'''

	def __init__(self, screen, left: int, top: int, width: int, height: int):
		super().__init__(left, top, width, height)
		self._screen = screen

	@property
	def screen(self)->pg.Surface:
		return self._screen

	def clear(self):
		pg.draw.rect(self.screen, BACKGROUND_COLOR, self)
		self.draw()
		pg.display.update()