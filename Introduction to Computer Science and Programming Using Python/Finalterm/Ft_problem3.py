# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 13:07:42 2018

@author: bianl
"""

def sum_digits(s):
    """ 
    assumes s a string
        
    Returns an int that is the sum of all of the digits in s.
          
    If there are no digits in s it raises a ValueError exception. 
    """
    assert type(s) is str
    sum = 0
    for i in range(len(s)):
        try:
            num = int(s[i])
        except:
            continue
        else:
           sum += num
    if sum == 0:
        raise ValueError 
    else:
        return sum
                   
    
print(sum_digits("a;d"))