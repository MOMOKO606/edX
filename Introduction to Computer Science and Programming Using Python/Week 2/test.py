# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 15:17:43 2018

@author: bianl
"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0
 
    returns: int or float, base^exp
    '''
    
    #  base case.
    if exp == 0:
        return 1
    if exp == 1:
        return base
    
    if exp % 2:
        return base * recurPower(base, exp//2) * recurPower(base, exp//2)
    else:
        return recurPower(base, exp/2) * recurPower(base, exp/2)
    
    

print(recurPower(2, 10))