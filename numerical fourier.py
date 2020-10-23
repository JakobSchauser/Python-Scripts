
import math
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos, pi

def integrate(f,a,b,q = 1000):
    area = 0
    w = abs(a-b)/q
    for i in range(q):
        area += w*f(a+i*w)
        
    return area


def fourier(f,T,o):
    c1,c2 = [],[]
    for i in range(o):
        g = lambda x : f(x)*cos(2*pi*i*x/T)
        c1.append((2/T)*integrate(g,-T/2,T/2))
        g = lambda x : f(x)*sin(2*pi*i*x/T)
        c2.append((2/T)*integrate(g,-T/2,T/2))
    return (c1,c2)

f = lambda x : x


a,b = fourier(f,10,4)

def F(x,a,b,T):
    funcs = []
    for xx in x:
        func = 0
        for i,(c1,c2) in enumerate(zip(a,b)):
            func += c1*cos(i*2*pi*xx/T) + c2*sin(i*xx*2*pi/T)
        funcs.append(func)
        
    return funcs

xr = np.linspace(-5,5,100)

plt.plot(xr,F(xr,a,b,5))
plt.plot(xr,list(map(f,xr)))
plt.show()