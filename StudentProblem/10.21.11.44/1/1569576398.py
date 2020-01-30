import functools
import typing
import string
import random
import pytest

def nwords(s: str) -> int:
    """Counts the numbers of words and returns it of a given string s"""
    b = 0
    w = 0
    for i in range(len(s)): #take every single element of string s
        if s[i] == True and not s[i] == " ": #if not space add element to b
            b = b + 1
        if s[i] == " ": #if space appears increase w (Word) by one
            if b > 0:  # word must be greater than zero to be approved as a word
                w = w + 1 # increase the number of words
                b = 0 # reset letter counter
    return w
        
            
            
            

    
