import pygame as pg
from drawElephantUtils import *

def _drawPoint(point, screen, minX, maxX, minY, maxY):

	xDimension, yDimension = screen.get_size()

	xPoint = point.getX() + (xDimension // 2)
	yPoint = point.getY() + (yDimension // 2)

	xRatio = (maxX - minX) / xDimension
	yRatio = (maxY - minY) / yDimension

	newX = xPoint * xRatio + minX
	newY = yPoint * yRatio + minY

	pg.draw.circle(screen, COLOR_LINE, (newX, newY), POINT_RADIUS)

def drawPoints(points, screen, minX, maxX, minY, maxY):

	for point in points:
		_drawPoint(point, screen, minX, maxX, minY, maxY)

	pg.display.update()