import turtle
import math
def circle(r):
    for i in range(100):
        turtle.forward(2*math.pi*r/ 100)
        turtle.left(360 / 100)

def duga(r):
    for i in range(50):
        turtle.forward(math.pi * r / 50)
        turtle.right(180 / 50)

turtle.color("orange")
turtle.begin_fill()
circle(100)
turtle.end_fill()

turtle.penup()
turtle.goto(50, 130)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
circle(15)
turtle.end_fill()

turtle.penup()
turtle.goto(-50, 130)
turtle.pendown()
turtle.color("green")
turtle.begin_fill()
circle(15)
turtle.end_fill()

turtle.penup()
turtle.goto(0, 100)
turtle.pendown()
turtle.color("black")
turtle.width(5)
turtle.right(90)
turtle.forward(30)

turtle.penup()
turtle.goto(40, 45)
turtle.pendown()
turtle.color("red")
turtle.width(8)
duga(40)
