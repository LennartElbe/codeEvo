import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """
    this function test if the number if palindrom
    
    Args:
    n(int): natural number
    
    Returns:
    True if the Numeber is palindromic and False if is not
    """
    result = str(n)
    if result [-1::-1] == str(n):
        return True
    else:
        return False
