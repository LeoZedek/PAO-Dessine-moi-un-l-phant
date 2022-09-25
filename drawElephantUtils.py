import math
from numpy import sqrt

AXES_WIDTH = 1

DISTANCE_BETWEEN_POINT = 1
POINT_RADIUS = 2

BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
DARK_GRAY = (100, 100, 100)

COLOR_AXES = DARK_GRAY
COLOR_LINE = BLACK

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.module = math.hypot(x, y)

		if x != 0:
			self.angle = math.atan(y / x)

		else:
			if y == 0:
				self.angle = 0

			elif y < 0:
				self.angle = -math.pi / 2

			else:
				self.angle = math.pi / 2
		
	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getModule(self):
		return self.module

	def getAngle(self):
		return self.angle

	def distance(self, point2):
		if self.getX() == point2.getX():
			return abs(self.getY() - point2.getY())

		if self.getY() == point2.getY():
			return abs(self.getX() - point2.getX())

		return math.hypot(self.getX() - point2.getX(), self.getY() - point2.getY())

	def linearEquation(self, point2):
		coeffA = (point2.getY() - self.getY()) / (point2.getX() - self.getX())
		coeffB = self.getY() - coeffA * self.getX()

		return coeffA, coeffB