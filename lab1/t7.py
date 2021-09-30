import turtle

a = 0
for i in range(400):
    turtle.forward(0.0005*a*4)
    turtle.left(4)
    a = a+4