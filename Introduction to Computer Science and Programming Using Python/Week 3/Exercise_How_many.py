# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 15:51:36 2018

@author: bianl

Exercise：How many
"""

animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')


def how_many(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: int, how many values are in the dictionary.
    '''
    count = 0
    for k in aDict:
        m = len(aDict[k])
        count += m
    return count

print(how_many(animals))