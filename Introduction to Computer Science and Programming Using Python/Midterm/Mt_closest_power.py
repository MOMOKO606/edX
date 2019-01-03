# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 13:22:00 2018

@author: bianl
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    
    Returns the exponent.
    
    For example,

    closest_power(3,12) returns 2
    closest_power(4,12) returns 2
    closest_power(4,1) returns 0
    '''
    #  Set initial value
    exp = -1
    mingap = None  
     
    while True:
        exp += 1
        delta = abs(num - base ** exp)
        #  First time case
        if mingap is None:
            mingap = delta
            res = exp
        else:
            if delta < mingap:
                mingap = delta
                res = exp
            else:
                break
    return res

print(closest_power(4,1))
                
        
        
        
        