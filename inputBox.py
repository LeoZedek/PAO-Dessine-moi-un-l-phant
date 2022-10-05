import pygame as pg
from drawElephantUtils import BLACK, BACKGROUND_COLOR, BOX_BORDER_WIDTH, BOX_BORDER_COLOR
from myRectangle import MyRectangle

# Function to verify that the pressed key is a digit
# Private function
def _isDigitKey(key):
	return key in range(pg.K_0, pg.K_9 + 1)

class InputBox(MyRectangle):
	'''
		Classe représentant une boite d'entrée dans laquelle, on peut mettre un nombre en entrée.
	'''

	def __init__(self, screen, left: int, top: int, width: int, height: int):
		super().__init__(screen, left, top, width, height)

	def draw(self):
		pg.draw.rect(self.screen, BOX_BORDER_COLOR, self, width = BOX_BORDER_WIDTH)
		pg.display.update()

	def setText(self, text):
		self.clear()

		letterSizeInPixels = self.height * 0.8
		letterSizeInPoints = round(letterSizeInPixels * 72 / 96  * 1.5)

		font = pg.font.SysFont(None, letterSizeInPoints)
		textToDisplay = font.render(text, True, BLACK)
		textWidth, textHeight = font.size(text)

		xDisplay = self.left + (self.width - textWidth) / 2
		yDisplay = self.top + (self.height - textHeight) / 2

		self.screen.blit(textToDisplay, (xDisplay, yDisplay))
		pg.display.update()

	def getNumberInput(self)->int:
		self.clear()

		notDone = True

		myNumber = ""

		while notDone:
			for event in pg.event.get():

				if event.type == pg.KEYDOWN:
					if _isDigitKey(event.key) and len(myNumber) < 4:
						myNumber += event.unicode
						self.setText(str(myNumber))

					if event.key == pg.K_RETURN:
						if len(myNumber) > 0:
							notDone = False

		return int(myNumber)