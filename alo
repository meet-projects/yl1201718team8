from turtle import *
import turtle
import math
import time
import random
from unit import Unit

turtle.ht()
turtle.bgcolor("black")
turtle.color("yellow")
turtle.write ("achtung" ,align = "center" , font = ("ariel" ,100 , "normal"))
time.sleep(2)
turtle.clear()
turtle.color("red")
turtle.pensize(10)

#---------------------------------------------
POS_LIST = []
POS_LIST2 = []
ALIVE = True
#to finish-----------------------------------|

RADIUS = 10
snake = turtle.clone()
snake2 = turtle.clone()
snake.shapesize(RADIUS / 10)
UP = 0
LEFT = 2
RIGHT = 3
direction = UP

def left():
	global direction
	direction = LEFT

def right():
	global direction
	direction = RIGHT

#################moving	
def move_left(event):
	snake.left(25)
getcanvas().bind("<Left>", move_left)

def move_right(event):
	snake.right(25)
getcanvas().bind("<Right>", move_right)
listen()

def collision():
	for i in range(len(POS_LIST)):
		if(i<len(POS_LIST)-10):
			distance = math.sqrt(math.pow(POS_LIST[i][0]-snake.xcor(), 2)+math.pow(POS_LIST[i][1]-snake.ycor(), 2))
			radius_sum = RADIUS + 10
			if(distance <= radius_sum):
				print("collide")
				snake.forward(10)
				return False

	return True


while(direction == LEFT):
	snake.left(25)
while(direction == RIGHT):
	snake.right(25)
#########################
count = 0
while(ALIVE == True):
	count += 1
	#new_unit = Unit(snake.xcor()-1,snake.ycor()-1, 10)
	POS_LIST.append(snake.pos())
	snake.stamp()
	snake.forward(2)
	ALIVE = collision()
	#SNAKEZ.append(new_unit)

# head = snakez[0], for others in snakez, if head.pos() == others.pos()

mainloop()