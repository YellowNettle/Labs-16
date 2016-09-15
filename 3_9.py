__author__ = 'student'
import turtle
turtle.shape('turtle')

def SM(n):
    a = 180 * n / (n - 2)
    i = 1
    while i <= n:
        turtle.forward(n)
        turtle.right(a)
         i += 1

s = 1
while s <= 10:
    SM(s)
    turtle.penup()
    turtle.forward(3)
    turtle.pendown()
    s += 1
