import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    """Computes whether a year is a leap year or not.
    
    Args:
        year: A natural number representing a year.
        
    Returns:
        bool True, if year is leap
        bool False, if year isn't leap
        
    """
    if year <= 1582:
        return False
    elif year % 4 == 0 and not(year % 100 == 0 and not year % 400  == 0):
        return True
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(2000) == True
    assert leap(2001) == False
    assert leap(1200) == False
######################################################################
