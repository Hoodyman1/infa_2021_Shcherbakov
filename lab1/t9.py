import turtle
import math
def MG(n,l):
    turtle.left(90 + 180/n)
    for i in range(n):
        turtle.forward(l)
        turtle.left(360/n)

def rad (n, a):
    r = a / (2 * math.sin(2*math.pi / (2 * n)))
    return r

l = 40
for i in range(1, 10, 1):
    MG((i+2), l + 5*i)
    turtle.right(180 / (i+2) + 90)
    turtle.penup()
    turtle.forward(rad(i+3, l + 5*(i+1)) - rad(i+2, l + 5*i))
    turtle.pendown()