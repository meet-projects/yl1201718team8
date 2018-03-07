from turtle import*
import random
import math
alive = True
red_surprise = clone()
blue_surprise = clone()
green_surprise = clone()
red_surprise.pu()
green_surprise.pu()
blue_surprise.pu()
#go thinner
def red_surprises():
	x_sup = random.randint(-340,340)
	y_sup = random.randint(-280,280)
	red_surprise.goto(x_sup,y_sup)
	red_surprise.color("Red")
	red_surprise.shape("circle")
	red_surprise.radius(15)
	



#makes you go fatter
def green_surprises():
	x_sup = random.randint(-340,340)
	y_sup = random.randint(-280,280)
	green_surprise.goto(x_sup,y_sup)
	green_surprise.color("Green")
	green_surprise.shape("circle")
	green_surprise.radius(15)
	
#683 ' 576' - screensize
red_surprises()
green_surprises()



def Gsurp_collide():
	Gdist = sqrt( (int(green_surprise.xcor()) - int(snake.xcor()))**2 + (int(green_surprise.ycor()) - int(snake.ycor()))**2 )
	if int(snake.radius()) + int(green_surprise.radius())>= Gdist:
		gcol = True
def Rsurp_collide():
	Rdist = sqrt( (int(red_surprise.xcor()) - int(snake.xcor()))**2 + (int(red_surprise.ycor()) - int(snake.ycor()))**2 )
	if int(snake.radius()) + int(red_surprise.radius())>= Rdist:
		rcol = True
if gcol:
	green_surprises()
	snake.radius(15)
if rcol:
	red_surprise()
	snake.radius(5)




_________________________________________

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
	red_surprise.radius(15)
	



#makes you go fatter
def green_surprises():
	x_sup = random.randint(-340,340)
	y_sup = random.randint(-280,280)
	green_surprise.goto(x_sup,y_sup)
	green_surprise.color("Green")
	green_surprise.shape("circle")
	green_surprise.radius(15)
	
#683 ' 576' - screensize
red_surprises()
green_surprises()



def Gsurp_collide():
	Gdist = sqrt( (int(green_surprise.xcor()) - int(snake.xcor()))**2 + (int(green_surprise.ycor()) - int(snake.ycor()))**2 )
	if int(snake.radius()) + int(green_surprise.radius())>= Gdist:
		gcol = True
def Rsurp_collide():
	Rdist = sqrt( (int(red_surprise.xcor()) - int(snake.xcor()))**2 + (int(red_surprise.ycor()) - int(snake.ycor()))**2 )
	if int(snake.radius()) + int(red_surprise.radius())>= Rdist:
		rcol = True
if gcol:
	green_surprises()
	snake.radius(15)
if rcol:
	red_surprise()
	snake.radius(5)