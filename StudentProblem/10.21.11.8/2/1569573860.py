import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """Checks if a given integer is a palindromic number or not.
    Args:
        n: an int(greater than 0)
    Returns:
        True or False
    """
    return n == str(x[::-1])
