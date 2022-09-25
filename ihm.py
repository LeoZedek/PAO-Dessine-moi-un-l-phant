import pygame as pg
from drawElephantUtils import *
from init_window import initWindow
from draw_points import drawPoints
from pointsAcquisition import getPoints

def clearScreen(screen):
	background = pg.Surface(screen.get_size())
	background = background.convert()
	background.fill(GRAY)

	screen.blit(background, (0, 0))

pg.init()

screen = initWindow()

points = getPoints(screen)

clearScreen(screen)

xDimension, yDimension = screen.get_size()

minXOriginalDrawing = 0
minYOriginalDrawing = 0

maxXOriginalDrawing = xDimension * PROPORTION_ORIGINAL_DRAWING
maxYOriginalDrawing = yDimension * PROPORTION_ORIGINAL_DRAWING

minXNewDrawing = maxXOriginalDrawing + 2
minYNewDrawing = maxYOriginalDrawing + 2

maxXNewDrawing = xDimension
maxYNewDrawing = yDimension

# Draw Border between drawing
for xAxis in range(xDimension):
	pg.draw.circle(screen, COLOR_AXES, (xAxis, maxYOriginalDrawing + 1), AXES_WIDTH)

for yAxis in range(yDimension):
	pg.draw.circle(screen, COLOR_AXES, (maxXOriginalDrawing + 1, yAxis), AXES_WIDTH)

drawPoints(points, screen, minXOriginalDrawing, maxXOriginalDrawing, minYOriginalDrawing, maxYOriginalDrawing)

notDone = True

while notDone:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			notDone = 0

		if event.type == pg.KEYDOWN:
			if event.key == pg.K_q:
				notDone = 0