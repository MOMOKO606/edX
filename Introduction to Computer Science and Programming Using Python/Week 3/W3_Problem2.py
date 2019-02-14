# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 10:02:15 2018

@author: bianl
"""

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    res =[]
    for i in range(len(secretWord)):
        if secretWord[i] in lettersGuessed:
            res.append(secretWord[i])
        else:
            res.append('_')
    return(''.join(res))
        
    
    




    
secretWord = 'apple' 
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print(getGuessedWord(secretWord, lettersGuessed))