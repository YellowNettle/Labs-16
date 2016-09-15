__author__ = 'student'
import turtle

turtle.shape('turtle')

def HC(n):
    i= 1
    while i <= 50:
        turtle.forward(n)
        turtle.right(3.6)
        i += 1

a = 5
b = 1
s = 1
while s <= 7:
    HC(a)
    HC(b)
    s += 1
