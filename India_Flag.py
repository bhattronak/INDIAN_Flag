import turtle
from turtle import*

#screen for output
screen = turtle.Screen()

# # Defining a turtle Instance
t = turtle.Turtle()
speed(0)

# initially penup()
t.penup()
t.goto(-300, 250)
t.pendown()

# Orange Rectangle
#white rectangle
t.color("orange")
t.begin_fill()
t.forward(600)
t.right(90)
t.forward(167)
t.right(90)
t.forward(600)
t.end_fill()
t.left(90)
t.color("white")
t.forward(167)

#Green Rectangle
t.color("green")
t.begin_fill()
t.forward(167)
t.left(90)
t.forward(600)
t.left(90)
t.forward(167)
t.end_fill()

# Creating black outer rectangle
t.color("black")
t.forward(167*2)
t.left(90)
t.forward(600)
t.left(90)
t.forward(167*3)
t.left(90)
t.forward(600)
t.left(90)
t.forward(167*1)

# Big Blue Circle
t.penup()
t.goto(70, 0)
t.pendown()
t.color("navy")
t.begin_fill()
t.circle(70)
t.end_fill()

# Big White Circle
t.penup()
t.goto(60, 0)
t.pendown()
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

# Mini Blue Circles
t.penup()
t.goto(-57, -8)
t.pendown()
t.color("navy")

	
# Small Blue Circle
t.penup()
t.goto(20, 0)
t.pendown()
t.begin_fill()
t.circle(20)
t.end_fill()
# Spokes
t.penup()
t.goto(0, 0)
t.pendown()
t.pensize(2)
for i in range(24):
	t.forward(60)
	t.backward(60)
	t.left(15)
	
#to hold the
#output window
turtle.done()
