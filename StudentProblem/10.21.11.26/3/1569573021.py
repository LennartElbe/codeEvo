import functools
import typing
import string
import random
import pytest

def leap(year: int):
    """Tells you if the given year is a leap year
    
    Args:
        year(int): an integer year > 1582
        
    Return:
        a bool value(True/False)"""
    if year >= 1582:
        if year % 4 == 0:
            if year % 100 == 0 and year % 400 != 0:
                    return False
            elif year % 100 == 0 and year % 400 == 0:
                return True
        else:
            return False
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert(leap(1584) == True)
######################################################################
