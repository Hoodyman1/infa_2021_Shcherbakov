import turtle
import math
def duga(r):
    for i in range(50):
        turtle.forward(math.pi * r / 50)
        turtle.right(180 / 50)
turtle.left(90)

for i in range(10):
    duga(50)
    duga(10)