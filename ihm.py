#!/usr/bin/env python3
import pygame as pg
from math import pi
from drawElephantUtils import *
from screenUtils import initWindow, clearScreen
from pointsAcquisition import getPoints, samplingPoints
from decompositionEnSerieDeFourier import decompositions_en_serie_de_fourier
from series_cercles import SeriesCercles
from point import Point2D
import time

from inputBox import InputBox
from drawingRectangle import DrawingRectangle

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

originalDrawingRectangle = DrawingRectangle(screen, leftOriginalDrawingRect, topOriginalDrawingRect, widthOriginalDrawingRect, heightOriginalDrawingRect)

## Construction of the reconstructed drawing rectangle

topReconstructedDrawingRect = heightOriginalDrawingRect - 1
leftReconstructedDrawingRect = widthOriginalDrawingRect - 1
widthReconstructedDrawingRect = xDimension - leftReconstructedDrawingRect + 1
heightReconstructedDrawingRect = yDimension - topReconstructedDrawingRect + 1

reconstructedDrawingRectangle = DrawingRectangle(screen, leftReconstructedDrawingRect, topReconstructedDrawingRect, widthReconstructedDrawingRect, heightReconstructedDrawingRect)

originalDrawingRectangle.drawBorder()
reconstructedDrawingRectangle.drawBorder()

originalDrawingRectangle.drawPoints(points)

## Construction of the input box

paddingTopBox = round(heightOriginalDrawingRect * INPUT_SAMPLING_BOX_PADDING_TOP)
paddingLeftBox = round(widthOriginalDrawingRect * INPUT_SAMPLING_BOX_PADDING_RIGHT)
boxHeight = round(INPUT_SAMPLING_BOX_HEIGHT * heightOriginalDrawingRect)
boxWidth = round(INPUT_SAMPLING_BOX_WIDTH * widthOriginalDrawingRect)

topSamplingBox = paddingTopBox
leftSamplingBox = widthOriginalDrawingRect + paddingLeftBox
samplingBoxHeight = boxHeight
samplingBoxWidth = boxWidth

samplingBox = InputBox(screen, leftSamplingBox, topSamplingBox, samplingBoxWidth, samplingBoxHeight)
samplingBox.draw()

numberCircleBoxHeight = boxHeight
numberCircleBoxWidth = boxWidth
topNumberCircleBox = topReconstructedDrawingRect - paddingTopBox - boxHeight
leftNumberCircleBox = xDimension - paddingLeftBox - boxWidth

numberCircleBox = InputBox(screen, leftNumberCircleBox, topNumberCircleBox, numberCircleBoxWidth, numberCircleBoxHeight)
numberCircleBox.draw()

startBoxHeight = boxHeight
startBoxWidth = boxWidth
topStartBox = topReconstructedDrawingRect + heightReconstructedDrawingRect // 2 - startBoxHeight // 2
leftStartBox = xDimension - paddingLeftBox - boxWidth

startBox = InputBox(screen, leftStartBox, topStartBox, startBoxWidth, startBoxHeight)
startBox.draw()
startBox.setText("GO !")

notDone = True

numberOfCircle = 0
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
                    numberOfPoints = samplingBox.getNumberInput()

                    sampledPoints = samplingPoints(points, numberOfPoints)
                    originalDrawingRectangle.clear()
                    originalDrawingRectangle.drawPoints(sampledPoints)

                elif numberCircleBox.collidepoint(event.pos):
                    numberOfCircle = numberCircleBox.getNumberInput()

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
    originalDrawingRectangle.drawPoints(sampledPoints)

    originalDrawingRectangle.draw()
    reconstructedDrawingRectangle.draw()

    pg.display.update()

    time.sleep(0.01)