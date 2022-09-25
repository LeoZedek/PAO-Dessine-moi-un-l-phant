import pygame as pg
from numpy import arange, linspace
from drawElephantUtils import *
from init_window import initWindow

# If the last two point of the points tab have a distance superior to DISTANCE_BETWEEN_POINT,
# a linear interpolation is made to add points between them.
# Private function
def _fixPoint(points, screen):

	xDimension, yDimension = screen.get_size()

	if len(points) > 1:

		end = len(points) - 1

		point1 = points[end - 1]
		point2 = points[end]

		distance = point1.distance(point2)
		nbPoints = distance // DISTANCE_BETWEEN_POINT

		if nbPoints > 0:

			if point1.getX() == point2.getX():

				yStep = distance / nbPoints

				if point1.getY() > point2.getY():
					yStep = -yStep

				# Not taking the first point because he is already in the points list.
				index = 0
				for newY in arange(point1.getY(), point2.getY(), yStep):
					if index > 0:
						pg.draw.circle(screen, COLOR_LINE, (point1.getX() + (xDimension // 2), newY + (yDimension // 2)), POINT_RADIUS)
						points.insert(len(points) - 1, Point(point1.getX(), newY))
					index += 1

				pg.display.update()


			else:
				
				coeffA, coeffB = point1.linearEquation(point2)

				xStep = (point2.getX() - point1.getX()) / nbPoints
				
				index = 0
				for newX in arange(point1.getX(), point2.getX(), xStep):
					if index > 0:
						newY = coeffA * newX + coeffB
						pg.draw.circle(screen, COLOR_LINE, (newX + (xDimension // 2), newY + (yDimension // 2)), POINT_RADIUS)
						points.insert(len(points) - 1, Point(newX, newY))
					index += 1

				pg.display.update()

def getPoints():

	pg.init()

	screen = initWindow()

	xDimension, yDimension = screen.get_size()

	# Draw axis
	for xAxis in range(xDimension):
		pg.draw.circle(screen, COLOR_AXES, (xAxis, yDimension // 2), AXES_WIDTH)

	for yAxis in range(yDimension):
		pg.draw.circle(screen, COLOR_AXES, (xDimension // 2, yAxis), AXES_WIDTH)

	pg.display.update()

	notDone = 1
	mouseDown = False
	points = []

	while notDone:

		for event in pg.event.get():
			if event.type == pg.QUIT:
				notDone = 0

			if event.type == pg.MOUSEBUTTONDOWN:
				mouseDown = True

			if event.type == pg.MOUSEBUTTONUP:
				mouseDown = False
				notDone = False

			if event.type == pg.MOUSEMOTION:
				if mouseDown:
					newPoint = Point(float(event.pos[0] - (xDimension // 2)), float(event.pos[1] - (yDimension // 2)))
					points.append(newPoint)
					pg.draw.circle(screen, COLOR_LINE, event.pos, POINT_RADIUS)

					_fixPoint(points, screen)

			if event.type == pg.KEYDOWN:
				print(event.key)
				if event.key == pg.K_q:
					notDone = False

					
		pg.display.update()

	if len(points) != 0:
		points.append(points[0])

		_fixPoint(points, screen)

	pg.quit()

	return points

def samplingPoints(points, numberOfPoints):

	pointsLength = len(points)

	if numberOfPoints > pointsLength:
		return points

	sampling = [points[round(i)] for i in linspace(0, pointsLength, numberOfPoints, endpoint = False)]

	return sampling