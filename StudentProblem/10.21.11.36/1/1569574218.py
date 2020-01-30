import functools
import typing
import string
import random
import pytest

def nwords(s: str) -> int:
    """Count the number of words in a given string. Words are separated by at least one char in string.whitespace
    Args:
        s (str): A string whose words are counted
    Returns: 
        int: Number of words in the given string
    """
    letters = string.ascii
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

