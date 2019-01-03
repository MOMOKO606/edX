# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 15:23:31 2018

@author: bianl
"""

#def f(a, b):
#    return a + b

def f(a, b):
    return a > b


def dict_diff( d1, d2 ):
    res = {}
    for key in d1.keys():
        if key not in d2.keys():
            res[key] = d1[key]
    for key in d2.keys():
        if key not in d1.keys():
            res[key] = d2[key]
    return res    
    

def dict_inter(d1, d2):
    res = {}
    for key in d1.keys():
        if key in d2.keys():
            res[key] = f(d1[key], d2[key])
    return res
        
    
def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    r1 = dict_inter(d1, d2)
    r2 = dict_diff( d1, d2 )
    return r1, r2
    
    
  
d1 = {1:30, 2:20, 3:30}
d2 = {1:40, 2:50, 3:60}
    
#d1 = {1:30, 2:20, 3:30, 5:80}
#
#d2 = {1:40, 2:50, 3:60, 4:70, 6:90}

print(dict_interdiff(d1, d2))