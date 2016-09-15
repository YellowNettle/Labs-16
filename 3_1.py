__author__ = 'student'
n = int(input())
a = 1
while a < n:
    if a % 2 == 0:
        print(a, 'even')
    else:
        print(a, 'odd')
    a += 1