# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 15:00:02 2018

@author: bianl
"""

def sumDigits(N):
    '''
    N: a non-negative integer
    
    return the sum of its digits.
    '''
    # Base case
    if N == 0:
        return 0
    return sumDigits(N // 10) +  N % 10

print(sumDigits(126))
    