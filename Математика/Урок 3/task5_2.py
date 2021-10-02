import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

fig = figure(figsize = (11, 11))
ax = Axes3D(fig)

a = 11
b = 111

X, Y = np.meshgrid((np.arange(-11, 11, 2)), (np.arange(-11, 11, 2)))

Z = b ** 2 + (b ** 2 * (X ** 2 / a ** 2))
Z1 = -(b ** 2 + (b ** 2 * (X ** 2 / a ** 2)))
Z2 = 2*a*X ** np.cos(40) + np.sqrt(2*a*X ** np.cos(40))
ax.plot_surface(X, Y, Z,  linewidth=1, color='g')
ax.plot_surface(X, Y, Z1,  linewidth=1, color='g')

u = np.linspace(0,2*np.pi, 32)
v = np.linspace(0, np.pi, 16)

x = 10 * np.outer(np.cos(u), np.sin(v))
y = 50 * np.outer(np.sin(u), np.sin(v))
z = -100 * np.outer(np.ones(np.size(u)), np.cos(v))

ax.plot_surface(x, y, z, rstride=4, cstride=4, color='r')


show()