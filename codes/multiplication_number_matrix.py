#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import numpy as np

def matrix_mult(p,n):

    s = np.zeros((n+1,n+1), dtype=np.int )
    m = np.zeros((n+1,n+1), dtype=np.int )

    for L in range(2, n+1):
        for i in range(1, n-L+2): 
            j = i+L-1
            m[i][j] = sys.maxsize 
        
            for k in range(i, j-1+1):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j] 

                if q < m[i][j]:
                    m[i][j] = q 
                    s[i][j] = k

    return m, s

def print_mult(s,i,j): 
    if i==j:
        print "A" + str(i) + "",
    else:
        print "(",
        print_mult(s,i,s[i][j]) 
        print " x ",
        print_mult(s,s[i][j]+1,j) 
        print ")",


def main():
    '''
    p1=[100,4,50,20,100] 
    
    m,s=matrix_mult(p1,len(p1)-1) 
    print_mult(s, 1, len(p1)-1)
    print("\nEl numero de multiplicaciones es: %d"%m[1][len(p1)-1])
    '''

    p2=[30,35,15,5,10,20,25]
    m,s=matrix_mult(p2,len(p2)-1) 
    print_mult(s, 1, len(p2)-1)
    print("\nEl numero de multiplicaciones es: %d"%m[1][len(p2)-1])

# Start program
if __name__ == "__main__":
    main()
