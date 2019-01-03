# -*- coding: utf-8 -*-
"""
Created on Sat Jul 21 14:18:37 2018

@author: bianl
"""

def uniqueValues(aDict):
    '''
    aDict: a dictionary
    
    returns a list of keys in aDict that map to integer values that are unique 
    (i.e. values appear exactly once in aDict). The list of keys you return should 
    be sorted in increasing order. (If aDict does not contain any unique values, 
    you should return an empty list.)
    '''
    # Auxiliary list & dictionary
    tmp_list = []  # Contains the unique values
    tmp_dict = {}  # Contains value : numbers of its occurrences 
    res = []

    for key,val in aDict.items():                      
        if val not in tmp_list:  #  Meet val at the first time
            tmp_list.append(val)
            tmp_dict[val] = 0
        else:
            tmp_dict[val] += 1
    for key,val in aDict.items():
        if tmp_dict[val] == 0:
            res.append(int(key))
    res.sort()         
    return res 
            
            
            
print(uniqueValues({1: 1, 2: 1, 3: 1}))            
        