__author__ = 'student'
import turtle

turtle.shape('turtle')

def CR(n):
    i= 1
    while i <= 100:
        turtle.forward(n)
        turtle.right(3.6)
        i += 1

def HC(n):
    i= 1
    while i <= 50:
        turtle.forward(n)
        turtle.left(3.6)
        i += 1

def EYE(n):
    turtle.color()
    turtle.begin_fill()
    CR(n)
    turtle.end_fill()

CR(5)
turtle.penup()
turtle.goto(-50, -50)
turtle.pendown()
EYE(1)
turtle.penup()
turtle.goto(55, -50)
turtle.pendown()
EYE(1)
turtle.penup()
turtle.goto(0, -55)
turtle.pendown()
turtle.width(7)
turtle.right(90)
turtle.forward(40)
turtle.penup()
turtle.goto(-45, -100)
turtle.pendown()
HC(3)