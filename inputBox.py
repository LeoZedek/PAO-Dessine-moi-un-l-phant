import pygame as pg

def isDigitKey(key):
	return key in range(pg.K_0, pg.K_9 + 1)

# Get the number input from the user with key input
# Max input is 99 999
def getNumberInput():

	notDone = True

	myNumber = ""

	while notDone:
		for event in pg.event.get():

			if event.type == pg.KEYDOWN:
				if isDigitKey(event.key) and len(myNumber) < 4:
					myNumber += event.unicode

				if event.key == pg.K_RETURN:
					notDone = False


	if len(myNumber) == 0:
		return None

	return int(myNumber)