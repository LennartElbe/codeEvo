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
            
            
    

