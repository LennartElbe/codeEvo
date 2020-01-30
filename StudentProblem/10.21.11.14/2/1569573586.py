import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """Function to test, if given number is palindromic
    
    Args:
        n: an integer
        
    Returns:
        True, if n is palindromic
        False, if n isnt
    """
    s = n[-1::-1]
    print(s)
