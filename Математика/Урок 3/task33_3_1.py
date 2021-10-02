import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pylab import *


def polar_decart(r,a):
    x = r*math.cos(a)
    y = r*math.sin(a)
    return x,y

polar_decart(2,45)