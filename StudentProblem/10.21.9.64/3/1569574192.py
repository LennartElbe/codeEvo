import functools
import typing
import string
import random
import pytest

def leap(jahreszahl: int) -> bool:
    """the schaltyear function
    
    Args:
    jahreszahl(int): natural number
    
    Returns:
    True is the number if a schaltyear or False if is not
    """
    if (jahreszahl % 4 == 0) and (jahreszahl > 1582):
        return True
    elif (jahreszahl % 100 == 0) and (jahreszahl % 400 != 0) and (jahreszahl > 1582):
        return False 
######################################################################
## Lösung Teil 2 (Tests)

def test_leap():
    """test the function leap"""
    assert(leap(2016)) == True
    assert(leap(1500)) == False
    assert(leap(2000)) == False
######################################################################
