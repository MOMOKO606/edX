# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 15:58:12 2018

@author: bianl

Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 

Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', 

your program should print:

Number of vowels: 5
"""
count = 0
for i in range(len(s)):
    x = s[i]
    if  x == 'a' or x == 'e' or x == 'i'or x == 'o' or x == 'u':
        count += 1
print("Number of vowels: " + str(count))
