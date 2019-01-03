# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 09:41:39 2018

@author: bianl
"""

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''   
    for i in range(len(secretWord)):
        if secretWord[i] not in lettersGuessed:
            return False
    return True
   
    
    
    
    
    
    
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(isWordGuessed(secretWord, lettersGuessed))