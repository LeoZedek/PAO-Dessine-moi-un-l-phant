import pygame as pg
from drawElephantUtils import BLACK, BACKGROUND_COLOR, DRAWING_RECT_BORDER_COLOR, DRAWING_RECT_BORDER_WIDTH
from drawElephantUtils import POINT_RADIUS, COLOR_LINE
from myRectangle import MyRectangle

class DrawingRectangle(MyRectangle):
	'''
		Classe représentant une boite d'entrée dans laquelle, on peut mettre un nombre en entrée.
	'''

	def __init__(self, screen, left: int, top: int, width: int, height: int):
		super().__init__(screen, left, top, width, height)

	def draw(self):
		self.drawBorder()	
		pg.display.update()

	def _drawPoint(self, point):

		xDimension, yDimension = self.screen.get_size()

		xPoint = point.abscisse + (xDimension // 2)
		yPoint = -point.ordonnee + (yDimension // 2)

		xRatio = self.width / xDimension
		yRatio = self.height / yDimension

		newX = xPoint * xRatio + self.left
		newY = yPoint * yRatio + self.top

		pg.draw.circle(self.screen, COLOR_LINE, (newX, newY), POINT_RADIUS)

	def drawPoints(self, points):
		for point in points:
			self._drawPoint(point)

		pg.display.update()

	def drawBorder(self):
		pg.draw.line(self.screen, DRAWING_RECT_BORDER_COLOR, (self.left, self.top), (self.left + self.width -1, self.top))
		pg.draw.line(self.screen, DRAWING_RECT_BORDER_COLOR, (self.left, self.top), (self.left, self.top + self.height -1))
		pg.draw.line(self.screen, DRAWING_RECT_BORDER_COLOR, (self.left + self.width - 1, self.top), (self.left + self.width - 1, self.top + self.height - 1))
		pg.draw.line(self.screen, DRAWING_RECT_BORDER_COLOR, (self.left, self.top + self.height - 1), (self.left + self.width - 1, self.top + self.height - 1))