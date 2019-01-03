# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 15:17:43 2018

@author: bianl
"""

r = 0.2 / 12
b = 3329
p = 310

tmp = b * r ** 12
minus = 0

for i in range(12,1,-1):
    minus += p * r ** i

print(tmp - minus)