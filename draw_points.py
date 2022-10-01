import pygame as pg
from drawElephantUtils import *
from rectangleUtils import clearRectangle

def _drawPoint(point, screen, drawingRectangle):

	xDimension, yDimension = screen.get_size()

	xPoint = point.x + (xDimension // 2)
	yPoint = point.y + (yDimension // 2)

	xRatio = drawingRectangle.width / xDimension
	yRatio = drawingRectangle.height / yDimension

	newX = xPoint * xRatio + drawingRectangle.left
	newY = yPoint * yRatio + drawingRectangle.top

	pg.draw.circle(screen, COLOR_LINE, (newX, newY), POINT_RADIUS)

def drawPoints(points, screen, drawingRectangle):
	clearRectangle(screen, drawingRectangle, COLOR_AXES, AXES_WIDTH)

	for point in points:
		_drawPoint(point, screen, drawingRectangle)

	pg.display.update()