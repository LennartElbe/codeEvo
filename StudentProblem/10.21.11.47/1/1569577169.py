import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s:str) -> int:
    """
    Calcualte the number of words in a string
    
    Args:
    s:str the string to be assesed
    
    Return:
    num:int the number of words in a atirng
    """
    num = 0
    LETTERS = [abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ]
    for i in s:
        if i not in LETTERS:
            num = num + 1
    return num
## Lösung Teil 2.
def word_count_iter(s:str) -> tuple:
    """
    Calculate number of lines, words and characters in a string
    
    Args:
    s:str the string to be assesed
    
    Return:
    A tuple containg the releveant data
    """
    lines = 0
    words = 0
    characters = 0
    for read in s:
        words = words + nwords(read)
        characters = chracters + len(list(s))
        lines = lines + 1
    return (lines, words, characters)
######################################################################
## Lösung Teil 3. (Tests)
def word_count_iter_test():
    string = "This a five word string."
    assert word_count_iter(string) == (1, 5, 24)
## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.
def word_count(f:str) -> tuple:
    obj = open(f, r)
    obj = obj.read()
    return word_count_iter(obj)
######################################################################
