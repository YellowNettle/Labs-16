__author__ = 'student'
import random
random.seed(0)
N = int(input())
i = 0
for n in range (1, N):
    a = random.uniform(-3, 3)
    if a >= -2 and a <= 2:
        y = a ** 2 + 4
    else:
        y = 0
    i += y
i = 6 * i / N
print(i)
