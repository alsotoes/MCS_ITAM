#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
from matplotlib.legend_handler import HandlerLine2D
from scipy.misc import factorial
import operator
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


length = 1000.0
step = 1.0

x0_axis = np.arange(0.0, length, step)
x_axis = np.arange(1.0, length, step)
x1_axis = np.arange(1.1, length, step)
'''
plt.figure(1)
line1, = plt.plot(x1_axis, np.log2( [ logstar(x) for x in x1_axis] ), label="Log(Log* n)")
line2, = plt.plot(x1_axis, [ 2**logstar(x) for x in x1_axis], label="2^(Log* n)")
line3, = plt.plot(x_axis, np.sqrt(np.full((1,len(x_axis)), 2, dtype=float))[0] ** np.log2(x_axis), label="sqrt(2) ^ Log n")
line4, = plt.plot(x0_axis, x0_axis**2, label="n^2")
line5, = plt.plot(x0_axis, factorial(x0_axis), label="n!")
line6, = plt.plot(x_axis, factorial(np.log2(x_axis)), label="(Log n)!")
line7, = plt.plot(x0_axis, (3/2)**x0_axis, label="(3/2)^n")
line8, = plt.plot(x0_axis, x0_axis**3, label="n^3")
line9, = plt.plot(x_axis, (np.log2(x_axis))**2, label="Log^2(n)")
line10, = plt.plot(x_axis, np.log2(factorial(x_axis)), label="Log(n!)")
line11, = plt.plot(x0_axis[:-100], (2**(2**x0_axis[:-100])), label="2^(2^n)") # Trim to avoid overflow warning
line12, = plt.plot(x1_axis, x1_axis**(1/np.log2(x1_axis)), label="n ^ (1/Log n)")
line13, = plt.plot(x1_axis, np.log(np.log(x1_axis)), label="Ln (Ln n)")
line14, = plt.plot(x0_axis, [ logstar(x) for x in x0_axis], label="Log* n")
line15, = plt.plot(x0_axis, x0_axis * (2**x0_axis), label="n * 2^n")
line16, = plt.plot(x1_axis, x1_axis**(np.log2(np.log2(x1_axis))), label="n^(log [log n])")
line17, = plt.plot(x_axis, np.log(x_axis), label="Ln n")
line18, = plt.plot(x0_axis, np.full((1,len(x0_axis)), 1, dtype=float)[0], label="1")
line19, = plt.plot(x_axis, 2**np.log2(x_axis), label="2^(Log n)")
line20, = plt.plot(x_axis, np.log2(x_axis)**np.log2(x_axis), label="(Log n)^(Log n)")
line21, = plt.plot(x0_axis, np.exp(x0_axis), label="exp (n)")
line22, = plt.plot(x_axis, 4**np.log2(x_axis), label="4^(Log n)")
line23, = plt.plot(x0_axis, factorial(x0_axis+1), label="(n+1)!")
line24, = plt.plot(x_axis, np.sqrt(np.log2(x_axis)), label="sqrt( Log n)")
line25, = plt.plot(x_axis, [ logstar(np.log2(x)) for x in x_axis], label="Log* (Log n)")
line26, = plt.plot(x_axis, 2**(np.sqrt(2*np.log2(x_axis))), label="2^sqrt(2 * Log n)")
line27, = plt.plot(x0_axis, x0_axis, label="n")
line28, = plt.plot(x0_axis, 2**x0_axis, label="2^n")
line29, = plt.plot(x_axis, x_axis*np.log2(x_axis), label="n*(Log n)")
line30, = plt.plot(x_axis[:-150], 2**(2**(x_axis[:-150]+1)), label="2^2^(n+1)") # Trim to avoid overflow warning
'''
# con val < 300 se tiene otro orden pero 'Log(n!)' => inf
#
val = 15000000000000000000

# Print values
graphs = []

#graphs.append(('grafica1', 'Log(Log* n)', np.log2(logstar(val)) )) #28
graphs.append(('grafica2', '2^(Log* n)', 2.0**logstar(val) ))
graphs.append(('grafica3', 'sqrt(2) ^ Log n', np.sqrt(2)**np.log2(val) ))
#graphs.append(('grafica4', 'n^2', val**2 )) #13
#graphs.append(('grafica5', 'n!', factorial(val) )) #4
#graphs.append(('grafica6', '(Log n)!', factorial(np.log2(val)) )) #11
#graphs.append(('grafica7', '(3/2)^n', (3.0/2.0)**val )) #8
#graphs.append(('grafica8', 'n^3', val**3 )) #12
graphs.append(('grafica9', 'Log^2(n)', (np.log2(val))**2 ))
graphs.append(('grafica10', 'Log(n!)', np.log2(factorial(val)) ))
#graphs.append(('grafica11', '2^(2^n)', 2**(2**val) )) #2
#graphs.append(('grafica12', 'n ^ (1/Log n)', val**(1.0/np.log2(val)) )) #29
graphs.append(('grafica13', 'Ln (Ln n)', np.log(np.log(val)) ))
graphs.append(('grafica14', 'Log* n', logstar(val) ))
#graphs.append(('grafica15', 'n * 2^n', val*(2**val) )) #6
#graphs.append(('grafica16', 'n^(log [log n])', val**(np.log2(np.log2(val))) )) #10
graphs.append(('grafica17', 'Ln n', np.log(val) ))
#graphs.append(('grafica18', '1', 1 )) #30
graphs.append(('grafica19', '2^(Log n)', 2**np.log2(val) ))
#graphs.append(('grafica20', '(Log n)^(Log n)', (np.log2(val))**(np.log2(val)) )) #9
#graphs.append(('grafica21', 'exp (n)', np.exp(val) )) #5
#graphs.append(('grafica22', '4^(Log n)', 4**np.log2(val) )) #14
#graphs.append(('grafica23', '(n+1)!', factorial(val+1) )) #3
graphs.append(('grafica24', 'sqrt( Log n)', np.sqrt(np.log(val)) ))
graphs.append(('grafica25', 'Log* (Log n)', logstar(np.log2(val)) ))
graphs.append(('grafica26', '2^sqrt(2 * Log n)', 2**(np.sqrt(2*np.log2(val))) ))
graphs.append(('grafica27', 'n', val ))
#graphs.append(('grafica28', '2^n', 2**val )) #7
graphs.append(('grafica29', 'n*(Log n)', val*np.log2(val) ))
#graphs.append(('grafica30', '2^2^(n+1)', 2**(2**(val+1)) )) #1

#print graphs
for graph in sorted(graphs, key=operator.itemgetter(2), reverse=True):
    print graph

'''
plt.legend(bbox_to_anchor=(0.95, 1), loc=2, borderaxespad=0.)
plt.setp(line1, linewidth=1.0)
plt.axis([0, length, 0, length])
plt.grid(True)
plt.show()
'''
