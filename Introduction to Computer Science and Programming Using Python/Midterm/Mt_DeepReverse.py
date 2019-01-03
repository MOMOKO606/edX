# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 14:07:04 2018

@author: bianl
"""

def deep_reverse(L):
    """ 
    assumes L is a list of lists whose elements are ints
    
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    
    It does not return anything.
    
    For example, if L = [[1, 2], [3, 4], [5, 6, 7]] 
    then deep_reverse(L) mutates L to be [[7, 6, 5], [4, 3], [2, 1]]
    """
    #  Reverse L
    L.reverse()
    #  Reverse each list in L
    for l in L:
        l.reverse()
    
    
    
L = [[1, 2], [3, 4], [5, 6, 7]]
print(deep_reverse(L))