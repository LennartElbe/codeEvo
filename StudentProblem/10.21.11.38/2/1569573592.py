import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int)-> bool:
    """this funtion tests if n is palindromic
    args: a number n
    returns: true if n is palindromic, false if n is not palindromic"""
    if n < 0:
        return False
    if repr(n) == repr(n)[-1 : 0]:
        return True
    else:
        return False

