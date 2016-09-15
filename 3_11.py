__author__ = 'student'
import turtle

turtle.shape('turtle')

def CR(n):
    i= 1
    while i <= 100:
        turtle.forward(n)
        turtle.right(3.6)
        i += 1
def CL(n):
    i = 1
    while i <= 100:
        turtle.forward(n)
        turtle.left(3.6)
        i += 1

a = 3
while a <= 12:
    CR(a)
    CL(a)
    a += 1