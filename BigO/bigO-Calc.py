#!/usr/bin/env python
# -*- coding: utf-8 -*-

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

# con val < 300 se tiene otro orden pero 'Log(n!)' => inf
#
val = 10000000000000000000

# Print values
graphs = []

# Ordenadas
#graphs.append(('grafica30', '2^2^(n+1)', 2**(2**(val+1)) )) #1
#graphs.append(('grafica11', '2^(2^n)', 2**(2**val) )) #2
#graphs.append(('grafica23', '(n+1)!', factorial(val+1) )) #3
#graphs.append(('grafica5', 'n!', factorial(val) )) #4
#graphs.append(('grafica21', 'exp (n)', np.exp(val) )) #5
#graphs.append(('grafica15', 'n * 2^n', val*(2**val) )) #6
#graphs.append(('grafica28', '2^n', 2**val )) #7
#graphs.append(('grafica7', '(3/2)^n', (3.0/2.0)**val )) #8
#graphs.append(('grafica20', '(Log n)^(Log n)', (np.log2(val))**(np.log2(val)) )) #9
#graphs.append(('grafica16', 'n^(log [log n])', val**(np.log2(np.log2(val))) )) #10
#graphs.append(('grafica6', '(Log n)!', factorial(np.log2(val)) )) #11
#graphs.append(('grafica8', 'n^3', val**3 )) #12
#graphs.append(('grafica4', 'n^2', val**2 )) #13
#graphs.append(('grafica22', '4^(Log n)', 4**np.log2(val) )) #14
#graphs.append(('grafica10', 'Log(n!)', np.log2(factorial(val)) )) #15 # en 171 ya  -> inf
######
### con variaciones (agregando 0s) hasta 10000000000000000000 se logro este orden
#graphs.append(('grafica29', 'n*(Log n)', val*np.log2(val) ))
#graphs.append(('grafica19', '2^(Log n)', 2**np.log2(val) ))
#graphs.append(('grafica27', 'n', val ))
#graphs.append(('grafica3', 'sqrt(2) ^ Log n', np.sqrt(2)**np.log2(val) ))
######
### Crecen lento, pero con diferencia considerable como para considerar el orden
#graphs.append(('grafica26', '2^sqrt(2 * Log n)', 2**(np.sqrt(2*np.log2(val))) ))
#graphs.append(('grafica9', 'Log^2(n)', (np.log2(val))**2 ))
######
### Crecen extremandamente lento y con diferencia despreciable entre ellas, por lo que no existe posibilidad de que cambien de orden
#graphs.append(('grafica17', 'Ln n', np.log(val) ))
#graphs.append(('grafica24', 'sqrt( Log n)', np.sqrt(np.log(val)) ))
#graphs.append(('grafica13', 'Ln (Ln n)', np.log(np.log(val)) ))
######
### Se vuelven estables cuando val -> inf ya que log* vale maximo 5
graphs.append(('grafica2', '2^(Log* n)', 2.0**logstar(val) ))
graphs.append(('grafica14', 'Log* n', logstar(val) ))
graphs.append(('grafica25', 'Log* (Log n)', logstar(np.log2(val)) ))
graphs.append(('grafica1', 'Log(Log* n)', np.log2(logstar(val)) )) #28
######
## Se ordenan por si solas por su bajo o nula crecimiento
graphs.append(('grafica12', 'n ^ (1/Log n)', val**(1.0/np.log2(val)) )) #29
graphs.append(('grafica18', '1', 1 )) #30

#print graphs
for graph in sorted(graphs, key=operator.itemgetter(2), reverse=True):
    print graph
