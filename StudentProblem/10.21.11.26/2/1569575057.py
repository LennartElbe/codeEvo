import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int):
    """Calculates if the given integer is a palindrome
    
    Args:
        n(int): an integer n > 0
    
    Return:
        a bool value(True/False)
    """
    if n > 0:
        n = str(n)
        if n == n[::-1]:
            return True
        else:
            return False
    else:
        return "Error, integer has to be > 0"
