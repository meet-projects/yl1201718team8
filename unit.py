from turtle import *
import math
import time
import random
<<<<<<< HEAD

ALIVE = True
class Unit(Turtle):
	def __init__(self, x, y):
		Turtle.__init__(self)
		self.x = x
		self.y = y
		self.ht()
		self.pu()
		self.shape("circle")
=======
class Unit():
	def __init__(self, x, y, radius):
		self.x = x
		self.y = y
		self.radius = radius


>>>>>>> 21833fd5f46c6de29540a47c34baf03406fac0f5
