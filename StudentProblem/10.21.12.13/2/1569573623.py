import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """Function to check if number is palindromic
    args: n: int number which gets tested
    """
    if n == n[-1::-1]:
        return True
    else:
        return False
    
