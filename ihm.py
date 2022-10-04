#!/usr/bin/env python3
import pygame as pg
from math import pi
from drawElephantUtils import *
from screenUtils import initWindow, clearScreen
from draw_points import drawPoints
from pointsAcquisition import getPoints, samplingPoints
from rectangleUtils import getNumberInput, drawRectangle, setRectangleText, clearRectangle
from decompositionEnSerieDeFourier import decompositions_en_serie_de_fourier
from series_cercles import SeriesCercles
from point import Point2D
import time

pg.init()

screen = initWindow()

points = getPoints(screen)

clearScreen(screen)

xDimension, yDimension = screen.get_size()

## Construction of the original drawing rectangle

topOriginalDrawingRect = 0
leftOriginalDrawingRect = 0
heightOriginalDrawingRect = yDimension * PROPORTION_ORIGINAL_DRAWING
widthOriginalDrawingRect = xDimension * PROPORTION_ORIGINAL_DRAWING

originalDrawingRectangle = pg.Rect(leftOriginalDrawingRect, topOriginalDrawingRect, widthOriginalDrawingRect, heightOriginalDrawingRect)

## Construction of the reconstructed drawing rectangle

topReconstructedDrawingRect = heightOriginalDrawingRect - 1
leftReconstructedDrawingRect = widthOriginalDrawingRect - 1
widthReconstructedDrawingRect = xDimension - leftReconstructedDrawingRect + 1
heightReconstructedDrawingRect = yDimension - topReconstructedDrawingRect + 1

reconstructedDrawingRectangle = pg.Rect(leftReconstructedDrawingRect, topReconstructedDrawingRect, widthReconstructedDrawingRect, heightReconstructedDrawingRect)

drawRectangle(screen, originalDrawingRectangle, COLOR_AXES,AXES_WIDTH)
drawRectangle(screen, reconstructedDrawingRectangle, COLOR_AXES, AXES_WIDTH)

drawPoints(points, screen, originalDrawingRectangle)

## Construction of the input box

paddingTopBox = round(heightOriginalDrawingRect * INPUT_SAMPLING_BOX_PADDING_TOP)
paddingLeftBox = round(widthOriginalDrawingRect * INPUT_SAMPLING_BOX_PADDING_RIGHT)
boxHeight = round(INPUT_SAMPLING_BOX_HEIGHT * heightOriginalDrawingRect)
boxWidth = round(INPUT_SAMPLING_BOX_WIDTH * widthOriginalDrawingRect)

topSamplingBox = paddingTopBox
leftSamplingBox = widthOriginalDrawingRect + paddingLeftBox
samplingBoxHeight = boxHeight
samplingBoxWidth = boxWidth

samplingBox = pg.Rect(leftSamplingBox, topSamplingBox, samplingBoxWidth, samplingBoxHeight)
drawRectangle(screen, samplingBox, BOX_BORDER_COLOR, BOX_BORDER_WIDTH)

numberCircleBoxHeight = boxHeight
numberCircleBoxWidth = boxWidth
topNumberCircleBox = topReconstructedDrawingRect - paddingTopBox - boxHeight
leftNumberCircleBox = xDimension - paddingLeftBox - boxWidth

numberCircleBox = pg.Rect(leftNumberCircleBox, topNumberCircleBox, numberCircleBoxWidth, numberCircleBoxHeight)
drawRectangle(screen, numberCircleBox, BOX_BORDER_COLOR, BOX_BORDER_WIDTH)

startBoxHeight = boxHeight
startBoxWidth = boxWidth
topStartBox = topReconstructedDrawingRect + heightReconstructedDrawingRect // 2 - startBoxHeight // 2
leftStartBox = xDimension - paddingLeftBox - boxWidth

startBox = pg.Rect(leftStartBox, topStartBox, startBoxWidth, startBoxHeight)
drawRectangle(screen, startBox, BOX_BORDER_COLOR, BOX_BORDER_WIDTH)
setRectangleText(screen, startBox, "GO !")

notDone = True

while notDone:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            notDone = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                notDone = False

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1: # If the button pressed is the left one
                if samplingBox.collidepoint(event.pos):
                    numberOfPoints = getNumberInput(screen, samplingBox)

                    sampledPoints = samplingPoints(points, numberOfPoints)
                    clearRectangle(screen, originalDrawingRectangle, COLOR_AXES, AXES_WIDTH)
                    drawPoints(sampledPoints, screen, originalDrawingRectangle)

                elif numberCircleBox.collidepoint(event.pos):
                    numberOfCircle = getNumberInput(screen, numberCircleBox)

                elif startBox.collidepoint(event.pos):
                    notDone = False

        pg.display.update()

sampledPointsComplexe = [complex(point) for point in sampledPoints]

coeffCN = decompositions_en_serie_de_fourier(sampledPointsComplexe, numberOfCircle)

centerReconstructedDrawing = Point2D(reconstructedDrawingRectangle.centerx, reconstructedDrawingRectangle.centery)
pas = 2*pi/1024
my_series_cercles = SeriesCercles(centerReconstructedDrawing, coeffCN, 1 - PROPORTION_ORIGINAL_DRAWING, pas, screen)
# print(coeffCN)
notDone = True

while notDone:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            notDone = False

        if event.type == pg.KEYDOWN:
            if event.key == pg.K_q:
                notDone = False

    clearScreen(screen)

    my_series_cercles.dessiner_le_chemin()
    my_series_cercles.dessiner_les_cercles()
    drawPoints(sampledPoints, screen, originalDrawingRectangle)

    drawRectangle(screen, originalDrawingRectangle, COLOR_AXES,AXES_WIDTH)
    drawRectangle(screen, reconstructedDrawingRectangle, COLOR_AXES, AXES_WIDTH)
    
    pg.display.update()

    time.sleep(0.01)
## Loop to draw
