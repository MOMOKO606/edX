# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 14:32:25 2018

@author: bianl

Exercise: genPrimes

Write a generator, genPrimes, that returns the sequence of prime numbers on successive

calls to its next() method: 2, 3, 5, 7, 11, ...

"""
def isPrimes(x , primes):
    """
    function: wether x is a prime number or not
    
    Input
    primes(list): 当前素数列表
    x(int):待测数
    
    Return: True if x is a prime number, False otherwise
    """
    for i in range(len(primes)):
        if x % primes[i] == 0:
            return False
    return True


def genPrimes():
    primes = [2]
    i = 0
    while True:
        yield primes[i]
        x = primes[i] + 1
        while not isPrimes(x, primes):
            x += 1
        primes.append(x)
        i += 1
        
        
foo = genPrimes()