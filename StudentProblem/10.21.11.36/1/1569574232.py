import functools
import typing
import string
import random
import pytest

## Lösung Teil 1.
def nwords(s: str) -> int:
    """Count the number of words in a given string. Words are separated by at least one char in string.whitespace
    Args:
        s (str): A string whose words are counted
    Returns: 
        int: Number of words in the given string
    """
    n = 0
    words = []
    current_word = ""
    for ch in s:
        if ch not in string.whitespace:
            current_word += ch
        else:
            if len(current_word) > 0:
                words.append(current_word)
                current_word = ""
    if len(current_word) > 0:
        words.append(current_word)
    return len(words)
                
print(nwords("Hello, World!"))               
            
         
        
        
        
# 'Hello, World'
# 2
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
