#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import numpy.matlib
import sys

def pivot(simplex_tableau):
    print "Calculating...."
    print simplex_tableau

    z = simplex_tableau[-1, :]
    
    enter_index = np.where(z[0] == np.min(z[0]))[1].item(0)
    z_coef = np.divide(simplex_tableau[:-1,-1], simplex_tableau[:-1, enter_index])
    print z_coef

    z_coef_min_index = np.where(z_coef == np.min(z_coef))[0][0]
    operational_pivot = simplex_tableau[z_coef_min_index][0].item(enter_index)

    print "\n"
    print "x: %d" % enter_index
    print "y: %d" % z_coef_min_index
    print "[%d,%d]: %d" % (enter_index, z_coef_min_index, operational_pivot)
    print "\n"

    operational_row = np.divide(simplex_tableau[z_coef_min_index], operational_pivot)

    '''
    print enter_index
    print operational_pivot
    print simplex_tableau
    print operational_row
    '''

    for i in range(simplex_tableau.shape[0]):
        '''
        print simplex_tableau[0].item(enter_index)
        print simplex_tableau[0]
        print operational_row
        '''

        #print numpy.subtract( simplex_tableau[i], np.multiply( operational_row, [simplex_tableau[i].item(enter_index)]) )
        if z_coef_min_index != i:
            simplex_tableau[i] = numpy.subtract( simplex_tableau[i], np.multiply( operational_row, [simplex_tableau[i].item(enter_index)]) )
        else:
            simplex_tableau[i] = np.divide(simplex_tableau[i], operational_pivot)

        #simplex_tableau[i, :] = simplex_tableau[i, :] - simplex_tableau[i, enter_index]*pivot

    '''
    pivot         = np.divide(simplex_tableau[leave_index, :], simplex_tableau[leave_index, enter_index])

    for i in range(tab_size[0]):
        simplex_tableau[i, :] = simplex_tableau[i, :] - simplex_tableau[i, enter_index]*pivot

    simplex_tableau[leave_index, :] = pivot

    return simplex_tableau
    '''
    #sys.exit()
    return simplex_tableau


def dantzig(A, b, z):
    mrange = A.shape[0] if A.shape[0] > A.shape[1] else A.shape[1]
    identity = np.matlib.identity(mrange)
    full_z = np.hstack([-z, np.zeros(mrange + 1)])
    simplex_tableau = np.hstack([A, identity, b])
    simplex_tableau = np.vstack([simplex_tableau, full_z])

    while np.sum(full_z < 0) != 0:
        simplex_tableau = pivot(simplex_tableau)
        full_z = simplex_tableau[-1, :]


# https://en.wikipedia.org/wiki/Simplex_algorithm
# Ax = b, xi >= 0
# z = f(x,y) => funcion a maximizar

A = np.array([[2,3],[4,1],[2,9]])
b = np.array([[25],[32],[54]])
z = np.array([21,31])

dantzig(A, b, z)
