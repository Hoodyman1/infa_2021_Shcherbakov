import turtle
import math
def circle(n, r):
    if n == 0:
        for i in range(100):
            turtle.forward(2*math.pi*r/ 100)
            turtle.left(360 / 100)
    if n == 1:
        for i in range(100):
            turtle.forward(2*math.pi*r/ 100)
            turtle.right(360 / 100)

turtle.left(90)
for i in range(10):
    circle(0, 10 + 10*i)
    circle(1, 10 + 10*i)