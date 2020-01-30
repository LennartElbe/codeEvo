import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int) -> bool:
    """
    Whether the given number n as string is a palindrome
    """
    assert n > 0
    return str(n) == str(n)[::-1]
