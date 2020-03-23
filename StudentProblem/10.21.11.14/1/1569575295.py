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

######################################################################
## Lösung Teil 3. (Tests)

## revert
try:
    word_count_iter = word_count_iter.__wrapped__
except:
    pass

## Lösung Teil 4.

######################################################################
