# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:32:25 2018

@author: bianl
"""
import string

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    res = list(string.ascii_lowercase)
    for i in range(len(lettersGuessed)):
        res.remove(lettersGuessed[i])
    return(''.join(res))
        
    
    


lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getAvailableLetters(lettersGuessed))
