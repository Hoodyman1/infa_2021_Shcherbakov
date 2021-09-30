import turtle

l = 50
for i in range(10):
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.forward(l)
    turtle.left(90)
    turtle.penup()
    turtle.goto(-(i+1)*10, -(i+1)*10)
    turtle.pendown()
    l = l+20