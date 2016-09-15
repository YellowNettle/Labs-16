__author__ = 'student'
import turtle

turtle.shape('turtle')

def CR(n):
    n = 1
    while n <= 100:
        turtle.forward(5)
        turtle.right(3.6)
        n += 1
def CL(n):
    n = 1
    while n <= 100:
        turtle.forward(5)
        turtle.left(3.6)
        n += 1

a = 1
while a <= 8:
    CR(a)
    CL(a)
    turtle.left(45)
    a += 1