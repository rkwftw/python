import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *

a = np.arange(0., 2., 1./180.)*np.pi

plt.polar(a, [10]*len(a))

plt.show()