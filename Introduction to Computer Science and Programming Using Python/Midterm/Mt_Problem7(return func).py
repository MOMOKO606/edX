# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 15:15:50 2018

@author: bianl
"""

def general_poly (L):
    """
    L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0
    """
    k = len(L) - 1
    def general_poly_Aux(x):
        sum = 0
        for i in range(0,len(L)):
            sum += L[k - i] * x ** i
        return sum   
    return general_poly_Aux

print(general_poly([1, 2, 3, 4])(10))