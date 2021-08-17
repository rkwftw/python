import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
k1 = 1
k2 = 2
plt.plot(x, np.cos(k1 * x))
plt.plot(x, np.cos(k2 * x))
plt.show()