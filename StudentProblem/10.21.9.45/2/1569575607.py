import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """
    Tests a given integer for palindromic state and returns a boolean.
    n: An integer
    """
    res = []
    if n > 0:
        res = str(n)
        if res[-1::-1] == str(n):
            return True
        else:
            return False
    else:
        return "Try a different number."
