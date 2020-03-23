import functools
import typing
import string
import random
import pytest

def leap(n: int) -> bool:
    """this functions checks whether a year is a leapyear
    args: n, a year number
    returns: true if n is a leapyear, false if n is not a leapyear"""
    if n % 4 == 0:
        return True
    elif n % 100 == 0 and n % 400 != 0:
        return False
      
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    """this function tests leap()"""
    assert leap(2000) == True
    assert leap(2002) == False

######################################################################
