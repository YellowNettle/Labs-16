__author__ = 'student'
__author__ = 'student'
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(-10, 10.01, 0.01)
y = (np.log((x**2 +1) * np.e ** (-abs(x) / 10))) / (np.log(1 + (np.tan(1 / (1 + np.sin(x)** 2)))))
plt.plot(x, y)
plt.show()