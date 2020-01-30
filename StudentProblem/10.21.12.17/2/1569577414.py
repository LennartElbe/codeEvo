import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """Computes whether a number is palindromic or not
    
    Args:
        n: A natural number
    
    Returns:
        bool True, if n is palindromic
        bool False, if n isn't palindromic
    
    """
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False
