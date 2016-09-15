__author__ = 'student'
import turtle

turtle.shape('turtle')

def SM(n):
    a = 180 * n / (n - 2)
    i = 1
    while i <= n:
        turtle.forward(35)
        turtle.right(180 - a)
        i += 1

f = 3
while f <= 10:
    SM(f)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()
    f += 1
