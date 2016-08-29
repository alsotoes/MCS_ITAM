import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
from scipy.misc import factorial
import numpy as np
import random
import math

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

figure = plt.figure(1)
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

plt.legend(handler_map={line1: HandlerLine2D(numpoints=1)})
plt.setp(line1, linewidth=1.0)
plt.axis([0, length, 0, length])
plt.grid(True)
##
figure = plt.figure(2)
line11, = plt.plot(x0_axis, (2**(2**x0_axis)), label="2^(2^n)")

plt.legend(handler_map={line11: HandlerLine2D(numpoints=1)})
plt.setp(line1, linewidth=1.0)
plt.axis([0, length, 0, length])
plt.grid(True)
plt.show()
