# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 13:25:21 2018

@author: bianl

Write a procedure called oddTuples, which takes a tuple as input, and returns a 

new tuple as output, where every other element of the input tuple is copied, 

starting with the first one. So if test is the tuple ('I', 'am', 'a', 'test', 'tuple'), 

then evaluating oddTuples on this input would return the tuple ('I', 'a', 'tuple').
"""

# def oddTuples(aTup):
#     '''
#     aTup: a tuple
#
#     returns: tuple, every other element of aTup.
#     '''
#     res = ()
#     for i in range(len(aTup)):
#         if i % 2 == 0:
#             res += (aTup[i],)  #  IMPORTANT!不能写成aTup[i]，tuple只能与tuple相加，所以要有(,)
#     return res


def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    res = [aTup[i] for i in range(len(aTup)) if i % 2 == 0 ]
    return tuple(res)

aTup = ('I', 'am', 'a', 'test', 'tuple')
res = oddTuples(aTup)        

