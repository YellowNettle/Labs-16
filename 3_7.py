__author__ = 'student'
import turtle

turtle.shape('turtle')
a = 10
n = 1
while n < 50:
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    a += 10
    n += 1