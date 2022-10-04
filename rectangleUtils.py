import pygame as pg
from drawElephantUtils import BLACK, BACKGROUND_COLOR, BOX_BORDER_WIDTH, BOX_BORDER_COLOR

# Function to verify that the pressed key is a digit
# Private function
def _isDigitKey(key):
	return key in range(pg.K_0, pg.K_9 + 1)

# Get the number input from the user with key input
# Max input is 9 999
def getNumberInput(screen, rectangle):
	clearRectangle(screen, rectangle, BOX_BORDER_COLOR, BOX_BORDER_WIDTH)

	notDone = True

	myNumber = ""

	while notDone:
		for event in pg.event.get():

			if event.type == pg.KEYDOWN:
				if _isDigitKey(event.key) and len(myNumber) < 4:
					myNumber += event.unicode
					setRectangleText(screen, rectangle, str(myNumber))

				if event.key == pg.K_RETURN:
					if len(myNumber) > 0:
						notDone = False

	return int(myNumber)

def setRectangleText(screen, rectangle, text):
	clearRectangle(screen, rectangle, BOX_BORDER_COLOR, BOX_BORDER_WIDTH)

	letterSizeInPixels = rectangle.height * 0.8
	letterSizeInPoints = round(letterSizeInPixels * 72 / 96  * 1.5)

	font = pg.font.SysFont(None, letterSizeInPoints)
	textToDisplay = font.render(text, True, BLACK)
	textWidth, textHeight = font.size(text)


	xDisplay = rectangle.left + (rectangle.width - textWidth) / 2
	yDisplay = rectangle.top + (rectangle.height - textHeight) / 2

	screen.blit(textToDisplay, (xDisplay, yDisplay))
	pg.display.update()

def drawRectangle(screen, rectangle, borderColor, borderWidth):	
	pg.draw.rect(screen, borderColor, rectangle, width = borderWidth)
	pg.display.update()

def clearRectangle(screen, rectangle, borderColor, borderWidth):
	pg.draw.rect(screen, BACKGROUND_COLOR, rectangle)
	drawRectangle(screen, rectangle, borderColor, borderWidth)
	pg.display.update()