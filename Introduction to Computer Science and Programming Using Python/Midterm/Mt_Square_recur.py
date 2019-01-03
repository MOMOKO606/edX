# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 20:57:59 2018

@author: bianl
"""

def Square(x):
    return SquareHelper(abs(x), abs(x))

def SquareHelper(n, x):
    if n == 0:
        return 0
    return SquareHelper(n-1, x) + x


print(Square(9))