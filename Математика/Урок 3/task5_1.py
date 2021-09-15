import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

fig = figure(figsize = (10, 10))
ax = Axes3D(fig)
X = np.arange(-10, 10, 2)
Y = np.arange(-10, 10, 2)

X, Y = np.meshgrid(X, Y)

Z = 10*X + 111
Z2 = 10*X + 11
ax.plot_wireframe(X, Y, Z, linestyle='--', linewidth=1)
ax.plot_wireframe(X, Y, Z2,colors='green')


show()