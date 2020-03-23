import functools
import typing
import string
import random
import pytest

def leap(x:int) -> bool:
    if x > 1582:
        if x%4 == 0:
            if (x%100 == and x%400 != 0):
                return False
            else: 
                return True
        return False
        
    else:
        return False
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    """ Test function for leap
    """
    assert leap(1581) == False
    assert leap(1600) == True
    assert leap(1800) == False
######################################################################
