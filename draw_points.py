import pygame as pg
from drawElephantUtils import *

def _drawPoint(point, screen, drawingRectangle):

	xDimension, yDimension = screen.get_size()

	xPoint = point.getX() + (xDimension // 2)
	yPoint = point.getY() + (yDimension // 2)

	xRatio = drawingRectangle.width / xDimension
	yRatio = drawingRectangle.height / yDimension

	newX = xPoint * xRatio + drawingRectangle.left
	newY = yPoint * yRatio + drawingRectangle.top

	pg.draw.circle(screen, COLOR_LINE, (newX, newY), POINT_RADIUS)

def drawPoints(points, screen, drawingRectangle):

	for point in points:
		_drawPoint(point, screen, drawingRectangle)

	pg.display.update()