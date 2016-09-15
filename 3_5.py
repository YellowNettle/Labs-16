__author__ = 'student'
import turtle

turtle.shape('turtle')
a = 30
while a <= 130:
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.penup()
    turtle.forward(5)
    turtle.left(90)
    turtle.forward(5)
    turtle.left(180)
    turtle.pendown()
    a += 10