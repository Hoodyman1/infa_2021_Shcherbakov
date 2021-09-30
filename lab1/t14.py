import turtle as t

def zvezda(n):
     for i in range(n):
        t.forward(100)
        t.left(180-180/n)

zvezda(11)