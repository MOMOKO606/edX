# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 12:52:40 2018

@author: bianl
"""

def union(set1, set2):
   """
   set1 and set2 are collections of objects, each of which might be empty.
   Each set has no duplicates within itself, but there may be objects that
   are in both sets. Objects are assumed to be of the same type.

   This function returns one set containing all elements from
   both input sets, but with no duplicates.
   """
   #  Base case
   if len(set1) == 0:
       return set2
   if set1[0] in set2[0]:
       return union(set1[1:],set2)
   else:
       return set1[0] + union(set1[1:],set2)