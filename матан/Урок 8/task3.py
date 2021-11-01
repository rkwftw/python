import numpy as np
from scipy.optimize import fsolve, broyden2
import math

def equations(xy):
    x = xy[0]
    y = xy[1]

    f = x**2-y**2+3*x*y**3-2*x**2*y**2+2*x-3*y-5
    g = 3*y**3-2*x**2+2*x**3*y-5*x**2*y**2+5
    return np.array([f,g])

xy0 = np.array([-100,100])
xy = fsolve(equations, xy0)
print(xy)

#Что-то у меня больше одной пары корней не попадается
for xy in np.arange (-2, 2, 0.001):
    #x =  fsolve(equations, x)
    #print (float(x))
    xy, info, ier, mesg =  fsolve(equations, xy0, full_output=True)
    print (xy, ier)

x = xy[0]
y = xy[1]
f = x**2-y**2+3*x*y**3-2*x**2*y**2+2*x-3*y-5
g = 3*y**3-2*x**2+2*x**3*y-5*x**2*y**2+5
print(f' Проверка: {f}, {g})