# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 12:18:41 2018

@author: bianl
"""
import random
import string


def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist


def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


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
            res.append('-')
    return(''.join(res))
  
    
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

    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''   
    n = len(secretWord)
    
    print("Welcome to the game Hangman!")
    print("I am thinking of a word that is " + str(n) +  " letters long")
    print("-----------")
    #  Set initial values
    ngl = 8 # number of guesses left
    lettersGuessed = [] 
    guesdlett = n * "-"
    
    while ngl > 0:
        print("You have " + str(ngl) + " guesses left.")
        availett = getAvailableLetters(lettersGuessed)
        print("Available letters:" + availett)
        key = input("Please guess a letter: ")
        key = key.lower()
        #  sentinel
        if key in lettersGuessed:
            print("Oops! You've already guessed that letter: " + guesdlett )
            print("------------")    
            continue
        
        lettersGuessed.append(key)
        guesdlett = getGuessedWord(secretWord, lettersGuessed)  # Guessed letter
            
        if key in secretWord:
            print("Good guess: " + guesdlett )
        else:
            ngl -= 1
            print("Oops! That letter is not in my word: " + guesdlett )
        print("------------")    
        #  sentinel
        if isWordGuessed(secretWord, lettersGuessed):
            print("Congratulations, you won!")
            return
    print("Sorry, you ran out of guesses. The word was else. ")
            

WORDLIST_FILENAME = "words.txt"
# Load the list of words into the variable wordlist
wordlist = loadWords()
# Pick a word in wordlist randomly
secretWord = chooseWord(wordlist)
hangman(secretWord)

