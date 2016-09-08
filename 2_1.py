import numpy as np
x = [1, 10, 1000]
e = np.e
s = np.sin(x)
c = 1 / (e ** s + 1)
z = 5 / 4 + 1 / (x ** 15)
d = c / z
a = numpy.log(d) / numpy.log(1 + x ** 2)
print (a)
