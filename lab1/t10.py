import turtle
import math
def circle(n):
    if n == 0:
        for i in range(200):
            turtle.forward(math.pi / 5)  # r=20
            turtle.left(360 / 200)
    if n == 1:
        for i in range(200):
            turtle.forward(math.pi / 5)  # r=20
            turtle.right(360 / 200)

circle(0)
circle(1)
turtle.left(60)
circle(0)
circle(1)
turtle.left(60)
circle(0)
circle(1)