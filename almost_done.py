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

####################surprises


red_surprise = clone()

green_surprise = clone()
red_surprise.pu()
green_surprise.pu()
red_surprise.showturtle()
green_surprise.showturtle()
#go thinner
def red_surprises():
	x_sup = random.randint(-340,340)
	y_sup = random.randint(-280,280)
	red_surprise.goto(x_sup,y_sup)
	red_surprise.color("Red")
	red_surprise.shape("circle")
	
	



#makes you go fatter
def green_surprises():
	x_sup = random.randint(-340,340)
	y_sup = random.randint(-280,280)
	green_surprise.goto(x_sup,y_sup)
	green_surprise.color("Green")
	green_surprise.shape("circle")
	
	
#683 ' 576' - screensize
red_surprises()
green_surprises()



def Gsurp_collide():
	Gdist = sqrt( (int(green_surprise.xcor()) - int(snake.xcor()))**2 + (int(green_surprise.ycor()) - int(snake.ycor()))**2 )
	if int(snake.radius()) + int(green_surprise.radius())>= Gdist:
		snake.radius(15)
def Rsurp_collide():
	Rdist = sqrt( (int(red_surprise.xcor()) - int(snake.xcor()))**2 + (int(red_surprise.ycor()) - int(snake.ycor()))**2 )
	if int(snake.radius()) + int(red_surprise.radius())>= Rdist:
		snake.radius(5)







######################################sdmfomlf
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
	Gsurp_collide()
	Rsurp_collide()
	

	#SNAKEZ.append(new_unit)

# head = snakez[0], for others in snakez, if head.pos() == others.pos()











mainloop()