#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
from scipy.misc import factorial
import numpy as np
import math


'''
https://en.wikipedia.org/wiki/Iterated_logarithm

x                | lg* x
-----------------|------
(−∞, 1]          | 0
(1, 2]           | 1
(2, 4]           | 2
(4, 16]          | 3
(16, 65536]      | 4
(65536, 2^65536] | 5
'''

def logstar(x):
    if x <= 1:
        return 0
    else:
        return 1 + logstar(math.log(x,2))


length = 20.0
step = 0.1

x0_axis = np.arange(0.0, length, step)
x_axis = np.arange(1.0, length, step)
x1_axis = np.arange(1.1, length, step)

plt.figure(1)
line1, = plt.plot(x1_axis, np.log( [ logstar(x) for x in x1_axis] ), label="Log(Log*)")
line2, = plt.plot(x1_axis, (2**np.log([ logstar(x) for x in x1_axis]))*np.log(x1_axis), label="2^(Log* n) * Log(n)")
line3, = plt.plot(x_axis, np.sqrt(np.full((1,len(x_axis)), 2, dtype=float))[0] * np.log(x_axis), label="sqrt(2) * Log(n)")
line4, = plt.plot(x0_axis, x0_axis**2, label="n^2")
line5, = plt.plot(x0_axis, factorial(x0_axis), label="n!")
line6, = plt.plot(x_axis, factorial(np.log(x_axis)), label="(Log n)!")
line7, = plt.plot(x0_axis, (3/2)**x0_axis, label="(3/2)^n")
line8, = plt.plot(x0_axis, x0_axis**3, label="n^3")
line9, = plt.plot(x_axis, (np.log(x_axis))**2, label="Log^2(n)")
line10, = plt.plot(x_axis, np.log(factorial(x_axis)), label="Log(n!)")
line11, = plt.plot(x0_axis, (2**(2**x0_axis)), label="2^(2^n)") # Overflow warning

plt.legend(bbox_to_anchor=(1.01, 1), loc=2, borderaxespad=0.)
plt.setp(line1, linewidth=1.0)
plt.axis([0, length, 0, length])
plt.grid(True)
plt.show()
