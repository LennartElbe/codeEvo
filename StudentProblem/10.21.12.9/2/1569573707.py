import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """Returns True, if n is al palindrom, else False
    Arguments:
        n: A positive Integer
    """
    n_str = str(n)
    n_str_reversed = n_str[::-1]
    if n_str == n_str_reversed:
        return True
    else:
        return False
