# -*- coding: utf-8 -*-
"""
Created on Sat Aug 25 13:52:50 2018

@author: bianl
"""
import math

def GSNGTK( L, n, j, key ):
    """
    Function: Get the Smallest Number Greater then the Key
    
    Input
    L: list of numbers
    n: Length of L
    j: Search starts at index j
    Key: a number
    
    Output
    The Smallest Number Greater then the Key and its index
    """
    
    # Set initial value
    min_greater_num = float("inf") 
    min_greater_index = j
    
    for k in range(j, n):        
        if L[k] >= key and L[k] < min_greater_num:
                min_greater_num = L[k]
                min_greater_index = k
    if math.isinf(min_greater_num) :
        return None, None
    else:
        return min_greater_num, min_greater_index
                            
    
def LMIS_brute(L, n):
    """
    Function: The brute force algorithm for Longest Monotonically Increasing Subsequence
    
    Input
    L: list of numbers
    n: Length of L
    
    Output
    The Longest Monotonically Increasing Subsequence
    """
    bestLMIS = []    
    for i in range(n):
        # the LMIS started at every element of L
        key = L[i]        
        LMIS = [key]  
        j = i + 1
        while j < n:
            [tmp, tmp_index] = GSNGTK(L[:], n, j, key)
            try:
                j = tmp_index + 1
                LMIS.append(tmp)                
                key = tmp
            except:
                break
        # Fix LMIS
        m = len(LMIS)
        for k in range(m-1, 1, -1):
            if LMIS[k - 1] != LMIS[k]:
                index = k 
                break
        try:
            LMIS_tmp = list(set(LMIS[: index]))
            LMIS = LMIS_tmp + LMIS[index :]
        except:
            LMIS = list(set(LMIS))
        
        #  Get bestLMIS   
        if len(LMIS) > len(bestLMIS):
            bestLMIS = LMIS
    return bestLMIS


def GLNSTK( L, n, j, key ):
    """
    Function: Get the Largest Number Smaller then the Key
    
    Input
    L: list of numbers
    n: Length of L
    j: Search starts at index j
    Key: a number
    
    Output
    The Largest Number Smaller then the Key and its index
    """
    
    # Set initial value
    max_smaller_num = float("-inf") 
    max_smaller_index = j
    
    for k in range(j, n):        
        if L[k] < key and L[k] > max_smaller_num:
                max_smaller_num = L[k]
                max_smaller_index = k
    if math.isinf(max_smaller_num) :
        return None, None
    else:
        return max_smaller_num, max_smaller_index
    

def LMDS_brute(L, n):
    """
    Function: The brute force algorithm for Longest Monotonically Decreasing Subsequence
    
    Input
    L: list of numbers
    n: Length of L
    
    Output
    The Longest Monotonically Decreasing Subsequence
    """
    bestLMDS = []    
    for i in range(n):
        # the LMDS started at every element of L
        key = L[i]        
        LMDS = [key]  
        j = i + 1
        while j < n:
            [tmp, tmp_index] = GLNSTK(L[:], n, j, key)
            try:
                j = tmp_index + 1
                LMDS.append(tmp)                
                key = tmp
            except:
                break       
        #  Get bestLMIS   
        if len(LMDS) > len(bestLMDS):
            bestLMDS = LMDS
    return bestLMDS


def longest_run(L):
    """
    Assumes L is a list of integers containing at least 2 elements.
    Finds the longest run of numbers in L, where the longest run can
    either be monotonically increasing or monotonically decreasing. 
    In case of a tie for the longest run, choose the longest run 
    that occurs first.
    Does not modify the list.
    Returns the sum of the longest run. 
    """
    n = len(L)
    LMIS = LMIS_brute(L, n)
    LMDS = LMDS_brute(L, n)

    if len(LMIS) > len(LMDS):
        return sum(LMIS)
    elif len(LMIS) < len(LMDS):
        return sum(LMDS)
    else:
        for k in range(len(L)):
            if L[k] == LMIS[0]:
                i = k
                break
        for k in range(len(L)):
            if L[k] == LMDS[0]:
                j = k
                break
        if i <= j:
            return sum(LMIS)
        else:
            return sum(LMDS)
               
#L = [10, 4, 3, 8, 3, 4, 5, 7, 7, 2]    
L = [5, 4, 10]    
print(longest_run(L))      