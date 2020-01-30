import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """checks an integer bigger than 0, if it is an palindrome. If yes, it returns True, else False.
       If the number n is smaller or equal than 0, it returns also False."""
    if n <= 0:
        return False
    n_str = str(n)
    if n_str == n_str[-1::-1]:
        return True
    else:
        return False
