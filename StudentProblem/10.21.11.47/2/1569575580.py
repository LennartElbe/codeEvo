import functools
import typing
import string
import random
import pytest

def is_palindromic(n:float) -> bool:
    """
    A function to test if n is palindromic.
    
    Args:
    n:float the decimal number to be tested.
    
    Return:
    A boolean indiciating if n is palindromic
    """
    left = ""
    right = ""
    decimal = 0
    for i in list(n):
        if i != ".":
            decimal = decimal + 1
    left = str(n)[:decimal]
    right = str(n)[decimal:]
    
    if reversed(left) == right:
        return true
    else:
        return false
    
