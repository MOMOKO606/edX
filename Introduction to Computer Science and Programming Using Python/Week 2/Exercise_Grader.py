# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 09:44:06 2018

@author: bianl

A regular polygon has n number of sides. Each side has length s.

The area of a regular polygon is: 0.25∗n∗s2tan(π/n)

The perimeter of a polygon is: length of the boundary of the polygon

Write a function called polysum that takes 2 arguments, n and s. 

This function should sum the area and square of the perimeter of the regular polygon. 

The function returns the sum, rounded to 4 decimal places.
"""

import math

def polysum(n,s):
    '''
    n: a positive integers, number of sides
    
    s: a positive integers, length of each sides
    
    returns: a positive integer, the sum of the area and squared perimeter of regular polygon
    '''
    perim = n * s    
    area = 0.25 * perim * s / math.tan(math.pi / n)
    return round(area + perim ** 2, 4)
    