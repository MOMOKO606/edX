# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:00:41 2018

@author: bianl

Exercise：biggest
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    maxlength = 0
    for k in aDict:
        m = len(aDict[k])
        if m > maxlength:
            res = k
    return res

print(biggest(animals))

