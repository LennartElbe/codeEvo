import functools
import typing
import string
import random
import pytest

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
