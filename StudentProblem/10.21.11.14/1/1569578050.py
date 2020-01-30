import functools
import typing
import string
import random
import pytest

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

