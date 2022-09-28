import pygame as pg
from drawElephantUtils import *
from init_window import initWindow
from draw_points import drawPoints
from pointsAcquisition import getPoints, samplingPoints
from inputBox import getNumberInput

def clearScreen(screen):
	background = pg.Surface(screen.get_size())
	background = background.convert()
	background.fill(GRAY)

	screen.blit(background, (0, 0))

def drawBox(screen, box, borderColor, borderWidth):	
	pg.draw.rect(screen, borderColor, box, width = borderWidth)
	pg.display.update()

def clearBox(screen, box, borderColor, borderWidth):
	pg.draw.rect(screen, BACKGROUND_COLOR, box)
	drawBox(screen, box, borderColor, borderWidth)
	pg.display.update()

pg.init()

screen = initWindow()

points = getPoints(screen)

clearScreen(screen)

xDimension, yDimension = screen.get_size()

topOriginalDrawingBox = 0
leftOriginalDrawingBox = 0

heightOriginalDrawingBox = yDimension * PROPORTION_ORIGINAL_DRAWING
widthOriginalDrawingBox = xDimension * PROPORTION_ORIGINAL_DRAWING

originalDrawingRectangle = pg.Rect(leftOriginalDrawingBox, topOriginalDrawingBox, widthOriginalDrawingBox, heightOriginalDrawingBox)
drawBox(screen, originalDrawingRectangle, COLOR_AXES,AXES_WIDTH)

drawPoints(points, screen, originalDrawingRectangle)

# Calculating the dimension and the coordinate of the rectangle of the sample input
topSamplingBox = round(heightOriginalDrawingBox * INPUT_SAMPLING_BOX_PADDING_TOP)
leftSamplingBox = round(widthOriginalDrawingBox * (1 + INPUT_SAMPLING_BOX_PADDING_RIGHT))
samplingBoxHeight = round(INPUT_SAMPLING_BOX_HEIGHT * heightOriginalDrawingBox)
samplingBoxWidth = round(INPUT_SAMPLING_BOX_WIDTH * widthOriginalDrawingBox)

samplingBox = pg.Rect(leftSamplingBox, topSamplingBox, samplingBoxWidth, samplingBoxHeight)

drawBox(screen, samplingBox, INPUT_SAMPLING_BOX_BORDER_COLOR, INPUT_SAMPLING_BOX_BORDER_WIDTH)

#drawBorderInputBox(screen, minXSamplingBox, maxXSamplingBox, minYSamplingBox, maxYSamplingBox)

notDone = True

while notDone:
	for event in pg.event.get():
		if event.type == pg.QUIT:
			notDone = 0

		if event.type == pg.KEYDOWN:
			if event.key == pg.K_q:
				notDone = 0

		if event.type == pg.MOUSEBUTTONDOWN:
			if event.button == 1: # If the button pressed is the left one
				if samplingBox.collidepoint(event.pos):
					clearBox(screen, samplingBox, INPUT_SAMPLING_BOX_BORDER_COLOR, INPUT_SAMPLING_BOX_BORDER_WIDTH)
					numberOfPoints = getNumberInput()

					sampledPoints = samplingPoints(points, numberOfPoints)
					clearBox(screen, originalDrawingRectangle, COLOR_AXES, AXES_WIDTH)
					drawPoints(sampledPoints, screen, originalDrawingRectangle)