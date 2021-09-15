import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

a = np.arange(4, 8, 2)
print(a)
b = np.arange(4, 8, 2)
print(b)

plt.polar(a, b)

plt.show()