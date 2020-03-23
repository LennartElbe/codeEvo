import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """Function to count words in a string s
    
    Args:
        s: a string
        
    Returns:
        Amount of words in the string s
        
    """
    counter = 0
    for i in s:
        if s != " ":
            counter += 1
    return counter
            
            
    
## Lösung Teil 2.
def word_count_iter(iterable: str) -> tuple:
    """Function to count the amount of lines, words and letters
    
    Args:
        iterable: a string
        
   Returns:
        amount of lines, words and letter
   """
   res = []
   lines = 0
   words = 0
   letters = 0
   for i in iterable:
    if 

######################################################################
## Lösung Teil 3. (Tests)
def test_empty():
    assert word_count_iter("") == [(lines, 0), (words, 0), (letters, 0)]

def test_norm():
    assert word_count_iter("Ab cd ef \n gh ij") == [(lines, 2), (words, 5), (letters, 10)]
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(f: str) -> tuple:
    """Function to return der number of lines, word and letters of a file
    
    Args:
        f: a string
    
    Returns:
        Number of lines, word and letter of f
    """
    file = open(f)
    word_count_iter(file)
######################################################################
