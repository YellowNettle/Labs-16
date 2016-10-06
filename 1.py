__author__ = 'student'
import random
import matplotlib.pyplot as plt

random.seed(0)
n1 = 100
values = [random.normalvariate(0, 1) for i in range(n1)]
plt.hist(values, bins = 100)
plt.show()

random.seed(0)
n2 = 1000
values = [random.normalvariate(0, 1) for i in range(n2)]
plt.hist(values, bins = 100)
plt.show()

random.seed(0)
n3 = 10000
values = [random.normalvariate(0, 1) for i in range(n3)]
plt.hist(values, bins = 100)
plt.show()

random.seed(0)
n4 = 100000
values = [random.normalvariate(0, 1) for i in range(n4)]
plt.hist(values, bins = 100)
plt.show()