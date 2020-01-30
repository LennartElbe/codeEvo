import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """Compute if an input number is palindromic or not.
    
    Args:
        n(int): A given number.
        
    Returns:
        True if n is palindromic False if not.
    """
    if str(n) == str(n)[-1::-1]:
        return True
    else:
        return False
