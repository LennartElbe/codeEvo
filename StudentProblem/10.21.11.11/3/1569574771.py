import functools
import typing
import string
import random
import pytest

def leap(year: int) -> bool:
    """
    Args: 
        year: an integer
        
    Returns:
        a boolean expression
     """
    if year < 1583:
        return False
    elif year % 4 == 0:
        if year % 100 == 0 and year %400 != 0:
            break
    else:
        return False
print(leap(1582))
print(leap(1600))

######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    assert leap(1582) == False
    assert leap(1583) == False
    assert leap(1600) == True
    assert leap(1644) == False
    assert 1644 % 400 != 0
######################################################################
