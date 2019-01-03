# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 00:15:47 2018

@author: bianl

Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur 

in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then

your program should print

Longest substring in alphabetical order is: abc

Note: This problem may be challenging. We encourage you to work smart. If you've 

spent more than a few hours on this problem, we suggest that you move on to a different 

part of the course. If you have time, come back to this problem after you've 

had a break and cleared your head.
"""
s = "avrwcmpu"
n = len(s)

i = 0
maxcount = 0
largeststr = []


while i < n and n-i >= maxcount:
    j = i
    largest = [s[j]]
    count = 1
    
    while j < n-1 and s[j] <= s[j+1] :
        largest.append(s[j+1])
        count += 1
        j += 1
        
    if count > maxcount:
        maxcount = count
        largeststr = largest
        
    i += 1


print("Longest substring in alphabetical order is: " + ''.join(largeststr))
    
