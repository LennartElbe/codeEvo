import functools
import typing
import string
import random
import pytest

def is_palindromic(n: int):
    """schaut noch ob due Zahl ein Palindrom ist
    Args: 
    n: ist eine Zahl"""
    if n > 0 and not n < 0:
        if str(n) == str(n[-1::-1])
            return True
    else:
        return False

