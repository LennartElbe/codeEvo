import functools
import typing
import string
import random
import pytest

def leap (x:int)->bool:
    """tests if a year x is a leapyear
        args: a year x
        returns: true if the year x is a leapyear, false otherwise """
    if x < 1582:
        return False
    if x % 4 == 0:
        if x % 100 == 0 and x % 400 != 0:
            return False
        else:
            return False
    else:
        return True
######################################################################
## Lösung Teil 2 (Tests)

def test():
    assert leap (1500) == False
    assert leap (2000) == True
    assert leap (2100) == False
    assert leap (1600) == True
    assert leap (1720) == False
######################################################################
