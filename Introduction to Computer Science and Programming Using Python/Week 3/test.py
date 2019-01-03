# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 22:09:48 2018

@author: bianl
"""
testList = [1, -4, 8, -9]

def applyToEach(L, f):
    for i in range(len(L)):
        L[i] = f(L[i])

def power(x):
    return x*x

applyToEach(testList, power)