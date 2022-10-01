#!/usr/bin/env python3
"""Module proposant la classe Point2D"""

from numpy import angle , abs
from math import hypot

class Point2D:
	def __init__(self, x: float, y: float):
		self._x = x
		self._y = y
		self._module  = abs(complex(self))
		self._argument = angle(complex(self))

	@property
	def x(self)->float:
		return self._x

	@property
	def y(self)->float:
		return self._y

	@property 
	def module(self)->float:
		return self._module

	@property
	def argument(self)->float:
		return self._argument

	def __complex__(self):
		return complex(self.x,self.y)

	def distance(self, point2):
		if self.x == point2.x:
			return abs(self.y - point2.y)

		if self.y == point2.y:
			return abs(self.x - point2.x)

		return hypot(self.x - point2.x, self.y - point2.y)
    
	def linearEquation(self, point2):
		coeffA = (point2.y - self.y) / (point2.x - self.x)
		coeffB = self.y - coeffA * self.x

		return coeffA, coeffB

            




    
