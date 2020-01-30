import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """Checks whether a given integer is palindromic.
    Args:
        n (int): A natural number > 0
    Returns:
        bool (Whether the given number is palindromic)
    """
    pal_list = [i for i in str(n)]
    return pal_list == pal_list[::-1]
