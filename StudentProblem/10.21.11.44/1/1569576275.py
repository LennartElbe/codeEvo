import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """Counts the numbers of words and returns it of a given string s"""
    b = 0
    w = 0
    for i in range(len(s)): #take every single element of string s
        if n[i] == True and not n[i] == " ": #if not space add element to b
            b = b + 1
        if n[i] == " ": #if space appears increase w (Word) by one
            if b > 0:  # word must be greater than zero to be approved as a word
                w = w + 1 # increase the number of words
                b = 0 # reset letter counter
    return w
        
            
            
            
## Lösung Teil 2.
def test_nwords():
    assert nwords("Mein Name ist Jan") == 4 #normal
    assert nwords("Mein Name istJan") == 3 #normal
    assert nwords("Hallo") == 1 #single word
    assert nwords(" ") == 0 # missing wird only withe space
    
######################################################################
## Lösung Teil 3. (Tests)

## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################
